"""\
Based on utrie2.h, utrie2.cpp from ICU

Created on Apr 28, 2020

@author Eric Mader
"""

from Utilities import isSurrogate, isSurrogateLead, isSurrogateTrail

class UTrie2(object):
    SHIFT_1 = 6 + 5
    SHIFT_2 = 5
    SHIFT_1_2 = SHIFT_1 - SHIFT_2

    OMITTED_BMP_INDEX_1_LENGTH = 0x10000 >> SHIFT_1
    CP_PER_INDEX_1_ENTRY = 1 << SHIFT_1

    INDEX_2_BLOCK_LENGTH = 1 << SHIFT_1_2
    INDEX_2_MASK = INDEX_2_BLOCK_LENGTH - 1

    DATA_BLOCK_LENGTH = 1 << SHIFT_2
    DATA_MASK = DATA_BLOCK_LENGTH - 1

    INDEX_SHIFT = 2
    DATA_GRANULARITY = 1 << INDEX_SHIFT
    INDEX_2_OFFSET = 0

    LSCP_INDEX_2_OFFSET = 0x10000 >> SHIFT_2
    LSCP_INDEX_2_LENGTH = 0x400 >> SHIFT_2
    INDEX_2_BMP_LENGTH = LSCP_INDEX_2_OFFSET + LSCP_INDEX_2_LENGTH
    UTF8_2B_INDEX_2_OFFSET = INDEX_2_BMP_LENGTH
    UTF8_2B_INDEX_2_LENGTH = 0x800 >> 6  # U+0800 is the first code point after 2-byte UTF-8

    INDEX_1_OFFSET = UTF8_2B_INDEX_2_OFFSET + UTF8_2B_INDEX_2_LENGTH

    BAD_UTF8_DATA_OFFSET = 0x80
    DATA_START_OFFSET = 0xC0

    def __init__(self, index, indexLength, index2NullOffset, dataNullOffset, highStart, highValueIndex, initialValue=0):
        self.index = index
        self.indexLength = indexLength
        self.dataLength = len(index) - indexLength
        self.index2NullOffset = index2NullOffset
        self.dataNullOffset = dataNullOffset
        self.highStart = highStart
        self.highValueIndex = highValueIndex
        self.initialValue = initialValue

    def indexRaw(self, offset, c):
        return ((self.index[offset + (c >> self.SHIFT_2)]) << self.INDEX_SHIFT) + (c & self.DATA_MASK)

    # # define _UTRIE2_INDEX_FROM_SUPP(trieIndex, c) \
    # (((int32_t)((trieIndex)[ \
    #                 (trieIndex)[(UTRIE2_INDEX_1_OFFSET - UTRIE2_OMITTED_BMP_INDEX_1_LENGTH) + \
    #                             ((c) >> UTRIE2_SHIFT_1)] + \
    #                 (((c) >> UTRIE2_SHIFT_2) & UTRIE2_INDEX_2_MASK)]) \
    #   << UTRIE2_INDEX_SHIFT) + \
    #  ((c) & UTRIE2_DATA_MASK))

    def indexFromSupp(self, c):
        index1 = (self.INDEX_1_OFFSET - self.OMITTED_BMP_INDEX_1_LENGTH) + (c >> self.SHIFT_1)
        index2 = self.index[index1] + ((c >> self.SHIFT_2) & self.INDEX_2_MASK)

        return (self.index[index2] << self.INDEX_SHIFT) + (c & self.DATA_MASK)

    # #define _UTRIE2_INDEX_FROM_CP(trie, asciiOffset, c) \
    # ((uint32_t)(c)<0xd800 ? \
    #     _UTRIE2_INDEX_RAW(0, (trie)->index, c) : \
    #     (uint32_t)(c)<=0xffff ? \
    #         _UTRIE2_INDEX_RAW( \
    #             (c)<=0xdbff ? UTRIE2_LSCP_INDEX_2_OFFSET-(0xd800>>UTRIE2_SHIFT_2) : 0, \
    #             (trie)->index, c) : \
    #         (uint32_t)(c)>0x10ffff ? \
    #             (asciiOffset)+UTRIE2_BAD_UTF8_DATA_OFFSET : \
    #             (c)>=(trie)->highStart ? \
    #                 (trie)->highValueIndex : \
    #                 _UTRIE2_INDEX_FROM_SUPP((trie)->index, c))
    def indexFromCodePoint(self, asciiOffset, c):
        if c < 0xD800:
            return self.indexRaw(0, c)

        if c <= 0xFFFF:
            offset = 0 if c > 0xDBFF else self.LSCP_INDEX_2_OFFSET - (0xD800 >> self.SHIFT_2)
            return self.indexRaw(offset, c)

        if c >= 0x10FFFF:
            return asciiOffset + self.BAD_UTF8_DATA_OFFSET

        return self.highValueIndex if c >= self.highStart else self.indexFromSupp(c)

    def get(self, c):
        return self.index[self.indexFromCodePoint(self.indexLength, c)]

    def enumerator(self, start=0, limit=0x110000, valueFunction=None):
        if not valueFunction: valueFunction = lambda v: v

        # get the enumeration value that corresponds to an initial-value trie data entry
        initialValue = valueFunction(self.initialValue)

        # set variables for previous range
        prevI2Block = -1
        prevBlock = -1
        prev = start
        prevValue = 0

        # enumerate index-2 blocks
        c = start
        while c < limit and c < self.highStart:
            tempLimit = min(c + self.CP_PER_INDEX_1_ENTRY, limit)

            if c <= 0xFFFF:
                if not isSurrogate(c):
                    i2Block = c >> self.SHIFT_2
                elif isSurrogateLead(c):
                    # Enumerate values for lead surrogate code points, not code units:
                    # This special block has half the normal length.
                    i2Block = self.LSCP_INDEX_2_OFFSET
                    tempLimit = min(0xDC00, limit)
                else:
                    # Switch back to the normal part of the index-2 table.
                    # Enumerate the second half of the surrogates block.
                    i2Block = 0xD800 >> self.SHIFT_2
                    tempLimit = min(0xE000, limit)
            else:
                # supplementary code point
                i2Block = self.index[(self.INDEX_1_OFFSET - self.OMITTED_BMP_INDEX_1_LENGTH) +
                              (c >> self.SHIFT_1)]

                if i2Block == prevI2Block and (c - prev) >= self.CP_PER_INDEX_1_ENTRY:
                    # The index-2 block is the same as the previous one, and filled with prevValue.
                    # Only possible for supplementary code points because the linear-BMP index-2
                    # table creates unique i2Block values.
                    c += self.CP_PER_INDEX_1_ENTRY
                    continue

            prevI2Block = i2Block
            if i2Block == self.index2NullOffset:
                # this is the null index-2 block
                if prevValue != initialValue:
                    if prev < c: yield range(prev, c), prevValue

                    prevBlock = self.nullBlock
                    prev = c
                    prevValue = initialValue

                c += self.CP_PER_INDEX_1_ENTRY
            else:
                # enumerate data blocks for one index-2 block
                i2Start = (c >> self.SHIFT_2) & self.INDEX_2_MASK

                if (c >> self.SHIFT_1) == (tempLimit >> self.SHIFT_1):
                    i2Limit = (tempLimit >> self.SHIFT_2) & self.INDEX_2_MASK
                else:
                    i2Limit = self.INDEX_2_BLOCK_LENGTH

                for i2 in range(i2Start, i2Limit+1):
                    block = self.index[i2Block + i2] << self.INDEX_SHIFT

                    if block == prevBlock and (c - prev) >= self.DATA_BLOCK_LENGTH:
                        # the block is the same as the previous one, and filled with prevValue
                        c += self.DATA_BLOCK_LENGTH
                        continue

                    prevBlock = block
                    if block == self.dataNullOffset:
                        # this is the null data block
                        if prevValue != initialValue:
                            if prev < c: yield range(prev, c), prevValue

                            prev = c
                            prevValue = initialValue

                        c += self.DATA_BLOCK_LENGTH
                    else:
                        for j in range(self.DATA_BLOCK_LENGTH):
                            value = valueFunction(self.index[block + j])
                            if value != prevValue:
                                if prev < c: yield range(prev, c), prevValue

                                prev = c
                                prevValue = value

                            c += 1

        if c > limit:
            c = limit  # could be higher if in the index2NullOffset
        elif c < limit:
            # c == highStart < limit
            value = valueFunction(self.index[self.highValueIndex])
            if value != prevValue:
                if prev < c: yield range(prev, c), prevValue

                prev = c
                prevValue = value

            c = limit

        # deliver last range
        if prev < c: yield range(prev, c), prevValue





