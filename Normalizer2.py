"""\
Based on Normalizer2.cpp, Normalizer2.h from ICU

Created on June 2, 2020

@author Eric Mader
"""

from Norm2NFCData import *
from CPTrie import CPTrie
from Utilities import isLead

# Fixed norm16 values.
MIN_YES_YES_WITH_CC = 0xfe02
JAMO_VT = 0xfe00
MIN_NORMAL_MAYBE_YES = 0xfc00
JAMO_L = 2  # offset=1 hasCompBoundaryAfter=FALSE
INERT = 1  # offset=0 hasCompBoundaryAfter=TRUE

# norm16 bit 0 is comp-boundary-after.
HAS_COMP_BOUNDARY_AFTER = 1
OFFSET_SHIFT = 1

# For algorithmic one-way mappings, norm16 bits 2..1 indicate the
# tccc (0, 1, >1) for quick FCC boundary-after tests.
DELTA_TCCC_0 = 0
DELTA_TCCC_1 = 2
DELTA_TCCC_GT_1 = 4
DELTA_TCCC_MASK = 6
DELTA_SHIFT = 3

MAX_DELTA = 0x40

# Byte offsets from the start of the data, after the generic header.
IX_NORM_TRIE_OFFSET = 0
IX_EXTRA_DATA_OFFSET = 1
IX_SMALL_FCD_OFFSET = 2
IX_RESERVED3_OFFSET = 3
IX_RESERVED4_OFFSET = 4
IX_RESERVED5_OFFSET = 5
IX_RESERVED6_OFFSET = 6
IX_TOTAL_SIZE = 7

# Code point thresholds for quick check codes.
IX_MIN_DECOMP_NO_CP = 8
IX_MIN_COMP_NO_MAYBE_CP = 9

# Norm16 value thresholds for quick check combinations and types of extra data.

# Mappings & compositions in [minYesNo..minYesNoMappingsOnly[.
IX_MIN_YES_NO = 10
# Mappings are comp-normalized.
IX_MIN_NO_NO = 11
IX_LIMIT_NO_NO = 12
IX_MIN_MAYBE_YES = 13

# Mappings only in [minYesNoMappingsOnly..minNoNo[.
IX_MIN_YES_NO_MAPPINGS_ONLY = 14
# Mappings are not comp-normalized but have a comp boundary before.
IX_MIN_NO_NO_COMP_BOUNDARY_BEFORE = 15
# Mappings do not have a comp boundary before.
IX_MIN_NO_NO_COMP_NO_MAYBE_CC = 16
# Mappings to the empty string.
IX_MIN_NO_NO_EMPTY = 17

IX_MIN_LCCC_CP = 18
IX_RESERVED19 = 19
IX_COUNT = 20

MAPPING_HAS_CCC_LCCC_WORD = 0x80
MAPPING_HAS_RAW_MAPPING = 0x40
# unused bit 0x20
MAPPING_LENGTH_MASK = 0x1f

# Korean Hangul and Jamo constants
JAMO_L_BASE = 0x1100     # "lead" jamo
JAMO_L_END = 0x1112
JAMO_V_BASE = 0x1161     # "vowel" jamo
JAMO_V_END = 0x1175
JAMO_T_BASE = 0x11a7     # "trail" jamo
JAMO_T_END = 0x11c2

HANGUL_BASE = 0xac00
HANGUL_END = 0xd7a3

JAMO_L_COUNT = 19
JAMO_V_COUNT = 21
JAMO_T_COUNT = 28

JAMO_VT_COUNT = JAMO_V_COUNT * JAMO_T_COUNT

HANGUL_COUNT = JAMO_L_COUNT * JAMO_V_COUNT * JAMO_T_COUNT
HANGUL_LIMIT = HANGUL_BASE + HANGUL_COUNT

minDecompNoCP = norm2_nfc_data_indexes[IX_MIN_DECOMP_NO_CP]
minCompNoMaybeCP = norm2_nfc_data_indexes[IX_MIN_COMP_NO_MAYBE_CP]
minLcccCP = norm2_nfc_data_indexes[IX_MIN_LCCC_CP]

minYesNo = norm2_nfc_data_indexes[IX_MIN_YES_NO]
minYesNoMappingsOnly = norm2_nfc_data_indexes[IX_MIN_YES_NO_MAPPINGS_ONLY]
minNoNo = norm2_nfc_data_indexes[IX_MIN_NO_NO]
minNoNoCompBoundaryBefore = norm2_nfc_data_indexes[IX_MIN_NO_NO_COMP_BOUNDARY_BEFORE]
minNoNoCompNoMaybeCC = norm2_nfc_data_indexes[IX_MIN_NO_NO_COMP_NO_MAYBE_CC]
minNoNoEmpty = norm2_nfc_data_indexes[IX_MIN_NO_NO_EMPTY]
limitNoNo = norm2_nfc_data_indexes[IX_LIMIT_NO_NO]
minMaybeYes = norm2_nfc_data_indexes[IX_MIN_MAYBE_YES]
assert (minMaybeYes & 7) == 0  # 8-aligned for noNoDelta bit fields
centerNoNoDelta = (minMaybeYes >> DELTA_SHIFT) - MAX_DELTA - 1

maybeYesCompositions = norm2_nfc_data_extraData
extraData = norm2_nfc_data_extraData[(MIN_NORMAL_MAYBE_YES-minMaybeYes)>>OFFSET_SHIFT:]

normTrie = CPTrie(norm2_nfc_data_trieIndex, norm2_nfc_data_trieData, norm2_nfc_data_type, norm2_nfc_data_valueWidth, \
                  norm2_nfc_data_index3NullOffset, norm2_nfc_data_dataNullOffset, norm2_nfc_data_highStart, norm2_nfc_data_shifted12HighStart)

def getNorm16(c):
    return INERT if isLead(c) else normTrie.get(c)

def getRawNorm16(c):
    return normTrie.get(c)

def isMaybeOrNonZeroCC(norm16):
    return norm16 >= minMaybeYes

def isDecompNoAlgorithmic(norm16):
    return norm16 >= limitNoNo

def isInert(norm16) :
    return norm16 == INERT

def isJamoL(norm16):
    return norm16 == JAMO_L

def isJamoVT(norm16):
    return norm16 == JAMO_VT

def hangulLVT():
    return minYesNoMappingsOnly | HAS_COMP_BOUNDARY_AFTER

def isHangulLV(norm16):
    return norm16 == minYesNo

def isHangulLVT(norm16):
        return norm16 == hangulLVT()

def hangulDecomposition(c):
    decomposition = ""
    c -= HANGUL_BASE
    c2 = c % JAMO_T_COUNT
    c //= JAMO_T_COUNT

    decomposition += chr(JAMO_L_BASE + c // JAMO_V_COUNT)
    decomposition += chr(JAMO_V_BASE + c % JAMO_V_COUNT)

    if c2 != 0:
        decomposition += chr(JAMO_T_BASE + c2)

    return decomposition

def rawHangulDecomposition(c):
    decomposition = ""
    orig = c
    c -= HANGUL_BASE
    c2 = c % JAMO_T_COUNT

    if c2 == 0:
        c //= JAMO_T_COUNT
        decomposition += chr(JAMO_L_BASE + c // JAMO_V_COUNT)
        decomposition += chr(JAMO_V_BASE + c % JAMO_V_COUNT)
    else:
        decomposition += chr(orig - c2)  # LV syllable
        decomposition += chr(JAMO_T_BASE + c2)

    return decomposition

def mapAlgorithmic(c, norm16):
        return c + (norm16 >> DELTA_SHIFT) - centerNoNoDelta

def getMappingIndex(norm16):
    return norm16 >> OFFSET_SHIFT

def stringFromData(index, length):
    s = ""
    lead = 0  # for the lead byte of a surrogate pair
    for i in range(length):
        ch = extraData[index + i]

        # handle surrogate pairs
        if lead != 0:
            ch = lead + (ch - 0xDC00 + 0x10000)
            lead = 0
        elif isLead(ch):
            lead = (ch - 0xD800) * 0x400
            continue

        s += chr(ch)

    return s


def getDecomosition(c):
    decomposition = ""
    norm16 = getNorm16(c)
    if c < minDecompNoCP or isMaybeOrNonZeroCC(norm16):
        # c does not decompose
        return None

    if isDecompNoAlgorithmic(norm16):
        # Maps to an isCompYesAndZeroCC.
        c = mapAlgorithmic(c, norm16)
        decomposition += chr(c)
        norm16 = getRawNorm16(c)

    if norm16 < minYesNo:
        return decomposition if len(decomposition) > 0 else None

    if isHangulLV(norm16) or isHangulLVT(norm16):
        # Hangul syllable: decompose algorithmically
        return hangulDecomposition(c)

    # c decomposes, get everything from the variable-length extra data
    ix = getMappingIndex(norm16)
    length = extraData[ix] & MAPPING_LENGTH_MASK

    decomposition += stringFromData(ix + 1, length)

    return decomposition

def getRawDecomposition(c):
    decomposition = ""
    norm16 = getNorm16(c)
    if c < minDecompNoCP or isMaybeOrNonZeroCC(norm16):
        # c does not decompose
        return None

    if isDecompNoAlgorithmic(norm16):
        c = mapAlgorithmic(c, norm16)
        decomposition += chr(c)
        return decomposition

    if norm16 < minYesNo:
        return decomposition if len(decomposition) > 0 else None

    if isHangulLV(norm16) or isHangulLVT(norm16):
        # Hangul syllable: decompose algorithmically
        return rawHangulDecomposition(c)

    # c decomposes, get everything from the variable-length extra data
    ix = getMappingIndex(norm16)
    firstUnit = extraData[ix]
    mLength = firstUnit & MAPPING_LENGTH_MASK
    if firstUnit & MAPPING_HAS_RAW_MAPPING:
        # Read the raw mapping from before the firstUnit
        # and before the optional ccc/lccc word.
        # Bit 7 = MAPPING_HAS_CCC_LCCC_WORD
        rawMappingIndex = ix - ((firstUnit >> 7) & 1) - 1
        rm0 = extraData[rawMappingIndex]

        if rm0 <= MAPPING_LENGTH_MASK:
            length = rm0
            ix = rawMappingIndex - rm0
        else:
            # Copy the normal mapping and replace its first two code units with rm0.
            decomposition += chr(rm0)
            ix += 3
            length = mLength - 2
    else:
        ix += 1
        length = mLength

    decomposition += stringFromData(ix, length)

    return decomposition

def stringToCharList(decomp):
    if not decomp: return None

    chars = [c for c in decomp]
    charList = ", ".join(chars)
    return f"[{charList}]"

def decompToCharList(c):
    return stringToCharList(getDecomosition(c))

def rawDecompToCharList(c):
    return stringToCharList(getRawDecomposition(c))

def test():
    print(f"getDecomposition('A') is {decompToCharList(ord('A'))}")
    print(f"getDecomposition('{chr(0x00A0)}') is {decompToCharList(0x00A0)}")
    print(f"getDecomposition('{chr(0x00A8)}') is {decompToCharList(0x00A8)}")
    print(f"getDecomposition('{chr(0x00C0)}') is {decompToCharList(0x00C0)}")
    print(f"getDecomposition('{chr(0x1EA6)}') is {decompToCharList(0x1EA6)}")
    print(f"getDecomposition('{chr(0x3307)}') is {decompToCharList(0x3307)}")
    print(f"getDecomposition('{chr(0xCA8D)}') is {decompToCharList(0xCA8D)}")
    print(f"getDecomposition('{chr(0xFA6C)}') is {decompToCharList(0xFA6C)}")
    print()

    print(f"getRawDecomposition('A') is {rawDecompToCharList(ord('A'))}")
    print(f"getRawDecomposition('{chr(0x00A0)}') is {rawDecompToCharList(0x00A0)}")
    print(f"getRawDecomposition('{chr(0x00A8)}') is {rawDecompToCharList(0x00A8)}")
    print(f"getRawDecomposition('{chr(0x00C0)}') is {rawDecompToCharList(0x00C0)}")
    print(f"getRawDecomposition('{chr(0x1EA6)}') is {rawDecompToCharList(0x1EA6)}")
    print(f"getRawDecomposition('{chr(0x3307)}') is {rawDecompToCharList(0x3307)}")
    print(f"getRawDecomposition('{chr(0xCA8D)}') is {rawDecompToCharList(0xCA8D)}")
    print(f"getRawDecomposition('{chr(0x6595)}') is {rawDecompToCharList(0x6595)}")
    print(f"getRawDecomposition('{chr(0xFA6C)}') is {rawDecompToCharList(0xFA6C)}")




if __name__ == "__main__":
    test()

