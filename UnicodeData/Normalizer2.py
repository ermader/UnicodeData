"""\
Based on normalizer2impl.cpp, normalizer2impl.h from ICU

Created on June 2, 2020

@author Eric Mader
"""

import struct
from Norm2NFCData import *
from ICUDataFile import ICUData
from CPTrie import CPTrie
from Utilities import isLead, charFromSurrogates

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

class Normalizer2(object):
    def __init__(self, trie, indexes, extraData):
        self.trie = trie

        self.minDecompNoCP = indexes[IX_MIN_DECOMP_NO_CP]
        self.minCompNoMaybeCP = indexes[IX_MIN_COMP_NO_MAYBE_CP]
        self.minLcccCP = indexes[IX_MIN_LCCC_CP]

        self.minYesNo = indexes[IX_MIN_YES_NO]
        self.minYesNoMappingsOnly = indexes[IX_MIN_YES_NO_MAPPINGS_ONLY]
        self.minNoNo = indexes[IX_MIN_NO_NO]
        self.minNoNoCompBoundaryBefore = indexes[IX_MIN_NO_NO_COMP_BOUNDARY_BEFORE]
        self.minNoNoCompNoMaybeCC = indexes[IX_MIN_NO_NO_COMP_NO_MAYBE_CC]
        self.minNoNoEmpty = indexes[IX_MIN_NO_NO_EMPTY]
        self.limitNoNo = indexes[IX_LIMIT_NO_NO]
        self.minMaybeYes = indexes[IX_MIN_MAYBE_YES]
        assert (self.minMaybeYes & 7) == 0  # 8-aligned for noNoDelta bit fields
        self.centerNoNoDelta = (self.minMaybeYes >> DELTA_SHIFT) - MAX_DELTA - 1

        extraDataStart = (MIN_NORMAL_MAYBE_YES - indexes[IX_MIN_MAYBE_YES]) >> OFFSET_SHIFT
        self.maybeYesCompositions = extraData[:extraDataStart]
        self.extraData = extraData[extraDataStart:]

    @classmethod
    def createFromHardCodedData(cls):
        trie = CPTrie(norm2_nfc_data_trieIndex, norm2_nfc_data_trieData, norm2_nfc_data_type, norm2_nfc_data_valueWidth, \
                      norm2_nfc_data_index3NullOffset, norm2_nfc_data_dataNullOffset, norm2_nfc_data_highStart, norm2_nfc_data_shifted12HighStart)

        return Normalizer2(trie, norm2_nfc_data_indexes, norm2_nfc_data_extraData)

    @classmethod
    def createFromFileData(cls, package):
        icuData = ICUData()

        dataOffset, dataHeader = icuData.getDataOffsetAndHeader(f"{package}.nrm")
        baseOffset = dataOffset + dataHeader.headerLength

        indicesStart = baseOffset
        indicesCount, = struct.unpack("I", icuData.getData(indicesStart, indicesStart + 4))
        indicesCount //= 4
        indicesLimit = indicesStart + (indicesCount * 4)
        indicesFormat = f"{indicesCount}I"
        indices = struct.unpack(indicesFormat, icuData.getData(indicesStart, indicesLimit))

        trieStart = indices[IX_NORM_TRIE_OFFSET] + baseOffset
        trieLimit = indices[IX_EXTRA_DATA_OFFSET] + baseOffset

        trie = CPTrie.createFromData(icuData.getData(trieStart, trieLimit))

        extraDataStart = trieLimit
        extraDataLimit = indices[IX_SMALL_FCD_OFFSET] + baseOffset
        extraDataLength = (extraDataLimit - extraDataStart) // 2
        extraDataFormat = f"{extraDataLength}H"
        extraData = struct.unpack(extraDataFormat, icuData.getData(extraDataStart, extraDataLimit))

        return Normalizer2(trie, indices, extraData)

    def getNorm16(self, c):
        return INERT if isLead(c) else self.trie.get(c)

    def getRawNorm16(self, c):
        return self.trie.get(c)

    def isMaybeOrNonZeroCC(self, norm16):
        return norm16 >= self.minMaybeYes

    def isDecompNoAlgorithmic(self, norm16):
        return norm16 >= self.limitNoNo

    def isDecompYes(self, norm16):
        return norm16 < self.minYesNo or self.minMaybeYes <= norm16

    def isInert(self, norm16) :
        return norm16 == INERT

    def isJamoL(self, norm16):
        return norm16 == JAMO_L

    def isJamoVT(self, norm16):
        return norm16 == JAMO_VT

    def hangulLVT(self):
        return self.minYesNoMappingsOnly | HAS_COMP_BOUNDARY_AFTER

    def isHangulLV(self, norm16):
        return norm16 == self.minYesNo

    def isHangulLVT(self, norm16):
            return norm16 == self.hangulLVT()

    def hangulDecomposition(self, c):
        decomposition = ""
        c -= HANGUL_BASE
        c2 = c % JAMO_T_COUNT
        c //= JAMO_T_COUNT

        decomposition += chr(JAMO_L_BASE + c // JAMO_V_COUNT)
        decomposition += chr(JAMO_V_BASE + c % JAMO_V_COUNT)

        if c2 != 0:
            decomposition += chr(JAMO_T_BASE + c2)

        return decomposition

    def rawHangulDecomposition(self, c):
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

    def mapAlgorithmic(self, c, norm16):
            return c + (norm16 >> DELTA_SHIFT) - self.centerNoNoDelta

    def getMappingIndex(self, norm16):
        return norm16 >> OFFSET_SHIFT

    def stringFromData(self, index, length):
        s = ""
        lead = 0  # for the lead byte of a surrogate pair
        for i in range(length):
            ch = self.extraData[index + i]

            # handle surrogate pairs
            if lead != 0:
                ch = charFromSurrogates(lead, ch)
                lead = 0
            elif isLead(ch):
                lead = ch
                continue

            s += chr(ch)

        return s


    def getDecomosition(self, c):
        decomposition = ""
        norm16 = self.getNorm16(c)
        if c < self.minDecompNoCP or self.isMaybeOrNonZeroCC(norm16):
            # c does not decompose
            return None

        if self.isDecompNoAlgorithmic(norm16):
            # Maps to an isCompYesAndZeroCC.
            c = self.mapAlgorithmic(c, norm16)
            decomposition += chr(c)
            norm16 = self.getRawNorm16(c)

        if norm16 < self.minYesNo:
            return decomposition if len(decomposition) > 0 else None

        decomposition = ""
        if self.isHangulLV(norm16) or self.isHangulLVT(norm16):
            # Hangul syllable: decompose algorithmically
            return self.hangulDecomposition(c)

        # c decomposes, get everything from the variable-length extra data
        ix = self.getMappingIndex(norm16)
        length = self.extraData[ix] & MAPPING_LENGTH_MASK

        decomposition += self.stringFromData(ix + 1, length)

        return decomposition

    def getRawDecomposition(self, c):
        decomposition = ""
        norm16 = self.getNorm16(c)
        if c < self.minDecompNoCP or self.isDecompYes(norm16):
            # c does not decompose
            return None

        if self.isHangulLV(norm16) or self.isHangulLVT(norm16):
            # Hangul syllable: decompose algorithmically
            return self.rawHangulDecomposition(c)

        if self.isDecompNoAlgorithmic(norm16):
            c = self.mapAlgorithmic(c, norm16)
            return chr(c)

        # c decomposes, get everything from the variable-length extra data
        ix = self.getMappingIndex(norm16)
        firstUnit = self.extraData[ix]
        length = firstUnit & MAPPING_LENGTH_MASK
        if firstUnit & MAPPING_HAS_RAW_MAPPING:
            # Read the raw mapping from before the firstUnit
            # and before the optional ccc/lccc word.
            # Bit 7 = MAPPING_HAS_CCC_LCCC_WORD
            rawMappingIndex = ix - ((firstUnit >> 7) & 1) - 1
            rm0 = self.extraData[rawMappingIndex]

            if rm0 <= MAPPING_LENGTH_MASK:
                length = rm0
                ix = rawMappingIndex - rm0
            else:
                # Copy the normal mapping and replace its first two code units with rm0.
                decomposition += chr(rm0)
                ix += 3
                length -= 2
        else:
            ix += 1

        if not decomposition and length == 0: return None

        decomposition += self.stringFromData(ix, length)

        return decomposition


def stringToCharList(decomp):
    if not decomp: return None

    chars = [c for c in decomp]
    charList = ", ".join(chars)
    return f"[{charList}]"

def decompToCharList(norm, c):
    return stringToCharList(norm.getDecomosition(c))

def rawDecompToCharList(norm, c):
    return stringToCharList(norm.getRawDecomposition(c))

def test():
    nfcTrie = Normalizer2.createFromHardCodedData()
    nfkcTrie = Normalizer2.createFromFileData("nfkc")
    nfkc_cfTrie = Normalizer2.createFromFileData("nfkc_cf")

    charList = [0x0041, 0x0061, 0x00A0, 0x00A8, 0x00AD, 0x00BE, 0x00C0, 0x00E0, 0x0178, 0x1EA6, 0x3307, 0x6569, 0xCA8D, 0xFA6C]

    print("NFC:")
    for ch in charList:
        print(f"getDecomposition('{chr(ch)}') is {decompToCharList(nfcTrie, ch)}")
    print()

    for ch in charList:
        print(f"getRawDecomposition('{chr(ch)}') is {rawDecompToCharList(nfcTrie, ch)}")
    print()

    print("NFKC:")
    for ch in charList:
        print(f"getDecomposition('{chr(ch)}') is {decompToCharList(nfkcTrie, ch)}")
    print()

    for ch in charList:
        print(f"getRawDecomposition('{chr(ch)}') is {rawDecompToCharList(nfkcTrie, ch)}")
    print()

    print("NFKC_CF:")
    for ch in charList:
        print(f"getDecomposition('{chr(ch)}') is {decompToCharList(nfkc_cfTrie, ch)}")
    print()

    for ch in charList:
        print(f"getRawDecomposition('{chr(ch)}') is {rawDecompToCharList(nfkc_cfTrie, ch)}")


if __name__ == "__main__":
    test()

