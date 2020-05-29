"""\
Based on ucptrie.cpp from ICU

Created on May 14, 2020

@author Eric Mader
"""
import struct
from fontTools.misc import sstruct
from Utilities import _object

UCPTRIE_SIG = 0x54726933  # "Tri3"

UCPTRIE_FAST_SHIFT = 6

# Number of entries in a data block for code points below the fast limit. 64=0x40 @internal
UCPTRIE_FAST_DATA_BLOCK_LENGTH = 1 << UCPTRIE_FAST_SHIFT

# Mask for getting the lower bits for the in-fast-data-block offset. @internal
UCPTRIE_FAST_DATA_MASK = UCPTRIE_FAST_DATA_BLOCK_LENGTH - 1

# @internal
UCPTRIE_SMALL_MAX = 0xfff

# Offset from dataLength (to be subtracted) for fetching the
# value returned for out-of-range code points and ill-formed UTF-8/16.
# @internal

UCPTRIE_ERROR_VALUE_NEG_DATA_OFFSET = 1

# Offset from dataLength (to be subtracted) for fetching the
# value returned for code points highStart..U+10FFFF.
# @internal

UCPTRIE_HIGH_VALUE_NEG_DATA_OFFSET = 2

# The length of the BMP index table. 1024=0x400
UCPTRIE_BMP_INDEX_LENGTH = 0x10000 >> UCPTRIE_FAST_SHIFT

UCPTRIE_SMALL_LIMIT = 0x1000
UCPTRIE_SMALL_INDEX_LENGTH = UCPTRIE_SMALL_LIMIT >> UCPTRIE_FAST_SHIFT

# Shift size for getting the index-3 table offset.
UCPTRIE_SHIFT_3 = 4

# Shift size for getting the index-2 table offset.
UCPTRIE_SHIFT_2 = 5 + UCPTRIE_SHIFT_3

# Shift size for getting the index-1 table offset.
UCPTRIE_SHIFT_1 = 5 + UCPTRIE_SHIFT_2

# Difference between two shift sizes,
# for getting an index-2 offset from an index-3 offset. 5=9-4

UCPTRIE_SHIFT_2_3 = UCPTRIE_SHIFT_2 - UCPTRIE_SHIFT_3

# Difference between two shift sizes,
# for getting an index-1 offset from an index-2 offset. 5=14-9

UCPTRIE_SHIFT_1_2 = UCPTRIE_SHIFT_1 - UCPTRIE_SHIFT_2

# Number of index-1 entries for the BMP. (4)
# This part of the index-1 table is omitted from the serialized form.

UCPTRIE_OMITTED_BMP_INDEX_1_LENGTH = 0x10000 >> UCPTRIE_SHIFT_1

# Number of entries in an index-2 block. 32=0x20
UCPTRIE_INDEX_2_BLOCK_LENGTH = 1 << UCPTRIE_SHIFT_1_2

# Mask for getting the lower bits for the in-index-2-block offset.
UCPTRIE_INDEX_2_MASK = UCPTRIE_INDEX_2_BLOCK_LENGTH - 1

# Number of code points per index-2 table entry. 512=0x200
UCPTRIE_CP_PER_INDEX_2_ENTRY = 1 << UCPTRIE_SHIFT_2

# Number of entries in an index-3 block. 32=0x20
UCPTRIE_INDEX_3_BLOCK_LENGTH = 1 << UCPTRIE_SHIFT_2_3

# Mask for getting the lower bits for the in-index-3-block offset.
UCPTRIE_INDEX_3_MASK = UCPTRIE_INDEX_3_BLOCK_LENGTH - 1

# Number of entries in a small data block. 16=0x10
UCPTRIE_SMALL_DATA_BLOCK_LENGTH = 1 << UCPTRIE_SHIFT_3

# Mask for getting the lower bits for the in-small-data-block offset.
UCPTRIE_SMALL_DATA_MASK = UCPTRIE_SMALL_DATA_BLOCK_LENGTH - 1

UCPTRIE_TYPE_ANY = -1
UCPTRIE_TYPE_FAST = 0  # Fast/simple/larger BMP data structure. Use functions and "fast" macros.
UCPTRIE_TYPE_SMALL = 1  # Small/slower BMP data structure. Use functions and "small" macros.

UCPTRIE_VALUE_BITS_ANY = -1
UCPTRIE_VALUE_BITS_16 = 0  # The trie stores 16 bits per data value.
UCPTRIE_VALUE_BITS_32 = 1  # The trie stores 32 bits per data value.
UCPTRIE_VALUE_BITS_8 = 2  # The trie stores 8 bits per data value.

UCPTRIE_OPTIONS_DATA_LENGTH_MASK = 0xf000
UCPTRIE_OPTIONS_DATA_NULL_OFFSET_MASK = 0xf00
UCPTRIE_OPTIONS_RESERVED_MASK = 0x38
UCPTRIE_OPTIONS_VALUE_BITS_MASK = 7

# Value for index3NullOffset which indicates that there is no index-3 null block.
# Bit 15 is unused for this value because this bit is used if the index-3 contains
# 18-bit indexes.
UCPTRIE_NO_INDEX3_NULL_OFFSET = 0x7fff
UCPTRIE_NO_DATA_NULL_OFFSET = 0xfffff

class CPTrie(object):
    _trieHeaderFormat = """
    # "Tri3" in big-endian US-ASCII (0x54726933)
    sig: I
    
    # Options bit field:
    # Bits 15..12: Data length bits 19..16.
    # Bits 11..8: Data null block offset bits 19..16.
    # Bits 7..6: UCPTrieType
    # Bits 5..3: Reserved (0).
    # Bits 2..0: UCPTrieValueWidth
    options: H
    
    # Total length of the index tables.
    indexLength: H
    
    # Data length bits 15..0.
    dataLength: H
    
    # Index-3 null block offset, 0x7fff or 0xffff if none.
    index3NullOffset: H
    
    # Data null block offset bits 15..0, 0xfffff if none. 
    dataNullOffset: H
    
    # First code point of the single-value range ending with U+10ffff,
    # rounded up and then shifted right by UCPTRIE_SHIFT_2.
    shiftedHighStart: H
    """
    _trieHeaderLength = sstruct.calcsize(_trieHeaderFormat)

    def __init__(self, trieData):
        trieHeader = sstruct.unpack(self._trieHeaderFormat, trieData[:self._trieHeaderLength], _object())

        self.type = (trieHeader.options >> 6) & 3  # There should be constants for these numbers...
        self.valueWidth = trieHeader.options & UCPTRIE_OPTIONS_VALUE_BITS_MASK
        self.indexLength = trieHeader.indexLength
        self.dataLength = ((trieHeader.options & UCPTRIE_OPTIONS_DATA_LENGTH_MASK) << 4) |trieHeader.dataLength
        self.index3NullOffset = trieHeader.index3NullOffset
        self.dataNullOffset = ((trieHeader.options & UCPTRIE_OPTIONS_DATA_NULL_OFFSET_MASK) << 8) | trieHeader.dataNullOffset
        self.highStart = trieHeader.shiftedHighStart << UCPTRIE_SHIFT_2
        self.shifted12HighStart = (self.highStart + 0xfff) >> 12
        actualLength = self._trieHeaderLength + self.indexLength * 2

        if self.valueWidth == UCPTRIE_VALUE_BITS_16:
            actualLength += self.dataLength * 2
        elif self.valueWidth == UCPTRIE_VALUE_BITS_32:
            actualLength += self.dataLength * 4
        else:
            actualLength += self.dataLength

        indexFormat = f"{self.indexLength}H"
        indexStart = self._trieHeaderLength
        indexLimit = indexStart + struct.calcsize(indexFormat)
        self.index = struct.unpack(indexFormat, trieData[indexStart:indexLimit])

        dataStart = indexLimit

        if self.valueWidth == UCPTRIE_VALUE_BITS_16:
            dataType = "H"
        elif self.valueWidth == UCPTRIE_VALUE_BITS_32:
            dataType = "I"
        else:
            dataType = "B"

        dataFormat = f"{self.dataLength}{dataType}"
        dataLimit = dataStart + struct.calcsize(dataFormat)
        self.data = struct.unpack(dataFormat, trieData[dataStart:dataLimit])

    def fastIndex(self, c):
        return self.index[c >> UCPTRIE_FAST_SHIFT] + (c & UCPTRIE_FAST_DATA_MASK)

    def internalSmallIndex(self, c):
        i1 = c >> UCPTRIE_SHIFT_1

        if self.type == type == UCPTRIE_TYPE_FAST:
            i1 += UCPTRIE_BMP_INDEX_LENGTH - UCPTRIE_OMITTED_BMP_INDEX_1_LENGTH
        else:
            i1 += UCPTRIE_SMALL_INDEX_LENGTH

        i3Block = self.index[self.index[i1] + ((c >> UCPTRIE_SHIFT_2) & UCPTRIE_INDEX_2_MASK)]
        i3 = (c >> UCPTRIE_SHIFT_3) & UCPTRIE_INDEX_3_MASK

        if (i3Block & 0x8000) == 0:
            # 16-bit indexes
            dataBlock = self.index[i3Block + i3]
        else:
            # 18-bit indexes stored in groups of 9 entries per 8 indexes.
            i3Block = (i3Block & 0x7fff) + (i3 & ~7) + (i3 >> 3)
            i3 &= 7
            dataBlock = (self.index[i3Block] << (2 + (2 * i3))) & 0x30000
            dataBlock |= self.index[i3Block + 1 + i3]

        return dataBlock + (c & UCPTRIE_SMALL_DATA_MASK)

    def smallIndex(self,c ):
        if c >= self.highStart:
            return self.dataLength - UCPTRIE_HIGH_VALUE_NEG_DATA_OFFSET
        return self.internalSmallIndex(c)

    def cpIndex(self, fastMax, c):
        if c <= fastMax:
            return self.fastIndex(c)

        if c <= 0x10FFFF:
            return self.smallIndex(c)

        return self.dataLength - UCPTRIE_ERROR_VALUE_NEG_DATA_OFFSET

    def get(self, c):
        if c <= 0x007F:
            dataIndex = c
        else:
            fastMax = 0xFFFF if self.type == UCPTRIE_TYPE_FAST else UCPTRIE_SMALL_MAX
            dataIndex = self.cpIndex(fastMax, c)

        return self.data[dataIndex]
