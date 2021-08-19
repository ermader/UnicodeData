"""\
Based on layout props code in uprops.cpp, uprops.h in ICU

Created on My 13, 2020

@author Eric Mader
"""

import struct

if __package__:
    from .ICUDataFile import ICUData
    from .CPTrie import CPTrie
    from UnicodeData import LayoutTypes
    from UnicodeData import EnumeratorTests
else:
    from ICUDataFile import ICUData
    from CPTrie import CPTrie
    import LayoutTypes
    import EnumeratorTests

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

(dataOffset, dataHeader) = id.getDataOffsetAndHeader("ulayout.icu")

baseOffset = dataOffset + dataHeader.headerLength

indicesStart = baseOffset
(indicesCount, ) = struct.unpack("I", id.getData(indicesStart, indicesStart+4))
indicesLimit = indicesStart + (indicesCount * 4)
indicesFormat = f"{indicesCount}I"
indices = struct.unpack(indicesFormat, id.getData(indicesStart, indicesLimit))

trieOffset = indicesLimit
trieLimit = indices[ULAYOUT_IX_INPC_TRIE_TOP] + baseOffset
trieData = id.getData(trieOffset, trieLimit)
inpcTrie = CPTrie.createFromData(trieData)

trieOffset = trieLimit
trieLimit = indices[ULAYOUT_IX_INSC_TRIE_TOP] + baseOffset
trieData = id.getData(trieOffset, trieLimit)
inscTrie = CPTrie.createFromData(trieData)

trieOffset = trieLimit
trieLimit = indices[ULAYOUT_IX_VO_TRIE_TOP] + baseOffset
trieData = id.getData(trieOffset, trieLimit)
voTrie = CPTrie.createFromData(trieData)

def getInPC(c):
    return inpcTrie.get(c)

def getInSC(c):
    return inscTrie.get(c)

def getVO(c):
    return voTrie.get(c)

