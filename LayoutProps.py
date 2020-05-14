"""\
Based on layout props code in uprops.cpp, uprops.h in ICU

Created on My 13, 2020

@author Eric Mader
"""

from ICUDataFile import ICUData, dataHeaderFormat, dataHeaderLength
import struct
from CPTrie import CPTrie

# Layout indexes indices
# Element 0 stores the length of the indexes[] array.
ULAYOUT_IX_INDEXES_LENGTH = 0
# Elements 1..7 store the tops of consecutive code point tries.
# No trie is stored if the difference between two of these is less than 16.
ULAYOUT_IX_INPC_TRIE_TOP = 1
ULAYOUT_IX_INSC_TRIE_TOP = 2
ULAYOUT_IX_VO_TRIE_TOP = 3
ULAYOUT_IX_RESERVED_TOP = 4

ULAYOUT_IX_TRIES_TOP = 7

ULAYOUT_IX_MAX_VALUES = 9

# Length of indexes[]. Multiple of 4 to 16-align the tries.
ULAYOUT_IX_COUNT = 12

id = ICUData()

dataOffset = id.getDataOffset("ulayout.icu")
layoutHeaderData = id.getData(dataOffset, dataOffset + dataHeaderLength)

(headerLength, magic1, magic2, infoSize, _, isBigEndian, charsetFamily, sizeofUChar, _, \
 dataFormat, fvMajor, fvMinor, fvMilli, fvMicro, dvMajor, dvMinor, dvMilli, dvMicro) = \
    struct.unpack(dataHeaderFormat, layoutHeaderData[:dataHeaderLength])

indicesStart = dataOffset + headerLength
(indicesCount, ) = struct.unpack("I", id.getData(indicesStart, indicesStart+4))
indicesLimit = indicesStart + (indicesCount * 4)
indicesFormat = f"{indicesCount}I"
indices = struct.unpack(indicesFormat, id.getData(indicesStart, indicesLimit))

trieOffset = indicesLimit
trieLimit = indices[ULAYOUT_IX_INPC_TRIE_TOP] + dataOffset + headerLength
trieData = id.getData(trieOffset, trieLimit)
inpcTrie = CPTrie(trieData)

trieOffset = trieLimit
trieLimit = indices[ULAYOUT_IX_INSC_TRIE_TOP] + dataOffset + headerLength
trieData = id.getData(trieOffset, trieLimit)
inscTrie = CPTrie(trieData)

trieOffset = trieLimit
trieLimit = indices[ULAYOUT_IX_VO_TRIE_TOP] + dataOffset + headerLength
trieData = id.getData(trieOffset, trieLimit)
voTrie = CPTrie(trieData)

def getInPC(c):
    return inpcTrie.get(c)

def getInSC(c):
    return inscTrie.get(c)

def getVO(c):
    return voTrie.get(c)

def test():
    print(f"getInPC(0x0901) is {getInPC(0x0901)}")
    print(f"getInPC(0x0915) is {getInPC(0x0915)}")
    print(f"getInPC(0x0B55) is {getInPC(0x0B55)}")
    print(f"getInSC('0') is {getInSC(ord('0'))}")

if __name__ == "__main__":
    test()
