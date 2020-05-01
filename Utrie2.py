"""\
Based on utrie2.h, utrie2.cpp from ICU

Created on Apr 28, 2020

@author Eric Mader
"""

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

    def __init__(self, index, indexLength, index2NullOffset, dataNullOffset, highStart, highValueIndex):
        self.index = index
        self.indexLength = indexLength
        self.dataLength = len(index) - indexLength
        self.index2NullOffset = index2NullOffset
        self.dataNullOffset = dataNullOffset
        self.highStart = highStart
        self.highValueIndex = highValueIndex

    def indexRaw(self, offset, c):
        return ((self.index[(offset) + (c >> self.SHIFT_2)]) << self.INDEX_SHIFT) + (c & self.DATA_MASK)

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
