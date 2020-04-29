
from PropsData import propsTrie_index, propsVectorsTrie_index, propsVectors, propsVectorColumns

UTRIE2_INDEX_SHIFT = 2
UTRIE2_SHIFT_1 = 6 + 5
UTRIE2_SHIFT_2 = 5
UTRIE2_DATA_BLOCK_LENGTH = 1 << UTRIE2_SHIFT_2
UTRIE2_DATA_MASK = UTRIE2_DATA_BLOCK_LENGTH - 1

class UTrie2(object):
    INDEX_SHIFT = 2
    SHIFT_1 = 6 + 5
    SHIFT_2 = 5
    DATA_BLOCK_LENGTH = 1 << UTRIE2_SHIFT_2
    DATA_MASK = UTRIE2_DATA_BLOCK_LENGTH - 1
    LSCP_INDEX_2_OFFSET = 0x10000 >> SHIFT_2,
    LSCP_INDEX_2_LENGTH = 0x400 >> SHIFT_2,
    BAD_UTF8_DATA_OFFSET = 0x80

    def __init__(self, index, indexLength, highStart, highValueIndex):
        self.index = index
        self.indexLength = indexLength
        # self.data = data
        self.highStart = highStart
        self.highValueIndex = highValueIndex
        self.dataLength = len(index) - indexLength

    def indexRaw(self, offset, c):
        return ((self.index[(offset)+((c)>>self.SHIFT_2)]) << self.INDEX_SHIFT) + ((c)&self.DATA_MASK)

    # # define _UTRIE2_INDEX_FROM_SUPP(trieIndex, c) \
    # (((int32_t)((trieIndex)[ \
    #                 (trieIndex)[(UTRIE2_INDEX_1_OFFSET - UTRIE2_OMITTED_BMP_INDEX_1_LENGTH) + \
    #                             ((c) >> UTRIE2_SHIFT_1)] + \
    #                 (((c) >> UTRIE2_SHIFT_2) & UTRIE2_INDEX_2_MASK)]) \
    #   << UTRIE2_INDEX_SHIFT) + \
    #  ((c) & UTRIE2_DATA_MASK))

    def indexFromSupp(self, c):
        pass

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

        return self.highValueIndex if c >= self.highStart else self.IndexFromSupp(c)

    def get(self, c):
        return self.index[self.indexFromCodePoint(self.indexLength, c)]

propsTrie = UTrie2(propsTrie_index, 4532, 0x110000, 0x5700)
propsVectorTrie = UTrie2(propsVectorsTrie_index, 5024, 0x110000, 0x79F8)


def getUnicodeProperties(c, column):
    if column > propsVectorColumns:
        return 0

    vecIndex = propsVectorTrie.get(c)
    return propsVectors[vecIndex+column]

kaRawIndex = propsTrie.indexFromCodePoint(0, 0x0915)
print(f"kaIndex = 0x{kaRawIndex:04X}")
print(f"kaValue = 0x{propsTrie.get(0x0915):04X}")