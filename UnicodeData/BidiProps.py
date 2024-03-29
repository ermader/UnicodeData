"""\
Based on ubidi_props.h, ubidi_props.cpp from ICU

Created on May 1, 2020

@author Eric Mader
"""

from .BidiPropsData import *
from .Utrie2 import UTrie2
from .uchar_h import *
# from .UCDTypeDictionaries import bidiClassNames
# from .UCDTypeDictionaries import joiningTypeNames as joiningTypes
# from .UCDTypeDictionaries import joiningGroupNames as joiningGroups
from .Utilities import arithmeticShift

#indices into the indexes array
UBIDI_IX_INDEX_TOP = 0
UBIDI_IX_LENGTH = 1
UBIDI_IX_TRIE_SIZE = 2
UBIDI_IX_MIRROR_LENGTH = 3

UBIDI_IX_JG_START = 4
UBIDI_IX_JG_LIMIT = 5
UBIDI_IX_JG_START2 = 6  # *new in format version 2.2, ICU 54
UBIDI_IX_JG_LIMIT2 = 7

UBIDI_MAX_VALUES_INDEX = 15,
UBIDI_IX_TOP = 16

# definitions for 16-bit bidi/shaping properties word
UBIDI_CLASS_SHIFT = 0  # bidi class: 5 bits (4..0)
UBIDI_JT_SHIFT = 5  # joining type: 3 bits (7..5)
UBIDI_BPT_SHIFT = 8  # Bidi_Paired_Bracket_Type(bpt): 2 bits (9..8)

UBIDI_JOIN_CONTROL_SHIFT = 10
UBIDI_BIDI_CONTROL_SHIFT = 11

UBIDI_IS_MIRRORED_SHIFT = 12  # 'is mirrored'
UBIDI_MIRROR_DELTA_SHIFT = 13  # bidi mirroring delta: 3 bits (15..13)
UBIDI_MIRROR_DELTA_BITS = 16 - UBIDI_MIRROR_DELTA_SHIFT

UBIDI_MAX_JG_SHIFT = 16  # max JG value in indexes[UBIDI_MAX_VALUES_INDEX] bits 23..16

UBIDI_CLASS_MASK = 0x0000001f
UBIDI_JT_MASK = 0x000000e0
UBIDI_BPT_MASK = 0x00000300

UBIDI_MAX_JG_MASK = 0x00ff0000

def getClassFromProps(props: int) -> int:
    return props & UBIDI_CLASS_MASK

def getFlagFromProps(props: int, shift: int) -> bool:
    return ((props >> shift) & 1) != 0

def getMirrorDeltaFromProps(props: int) -> int:
    return arithmeticShift(props, 16, UBIDI_MIRROR_DELTA_BITS)

UBIDI_ESC_MIRROR_DELTA = -4
UBIDI_MIN_MIRROR_DELTA = -3
UBIDI_MAX_MIRROR_DELTA = 3

# definitions of the 32-bit mirror table entry
# the source code takes 21 bits (20..0)
UBIDI_MIRROR_INDEX_SHIFT = 21
UBIDI_MAX_MIRROR_INDEX = 0x7ff

bidiPropsTrie = UTrie2(ubidi_props_trieIndex, ubidi_props_trie_index_length, ubidi_props_trie_index_2_null_offset, \
                       ubidi_props_trie_data_null_offset, ubidi_props_trie_high_start, ubidi_props_trie_high_value_index)

def getMirrorCodePointFromProps(m: int) -> int:
    return m & 0x1FFFFF

def getMirrorIndexFromProps(m: int) -> int:
    return m >> UBIDI_MIRROR_INDEX_SHIFT

def getCharDirection(c: int) -> int:
    props = bidiPropsTrie.get(c)
    return getClassFromProps(props)

def isMirrored(c: int) -> bool:
    props = bidiPropsTrie.get(c)
    return getFlagFromProps(props, UBIDI_IS_MIRRORED_SHIFT)

def getMirrorFromProps(c: int, props: int) -> int:
    delta = getMirrorDeltaFromProps(props)

    if delta != UBIDI_ESC_MIRROR_DELTA:
        return c + delta

    for m in ubidi_props_mirrors:
        c2 = getMirrorCodePointFromProps(m)

        if c == c2:
            mirrorIndex = getMirrorIndexFromProps(m)
            return getMirrorCodePointFromProps(ubidi_props_mirrors[mirrorIndex])

        if c < c2:
            break

    return c

def getMirror(c: int) -> int:
    props = bidiPropsTrie.get(c)
    return getMirrorFromProps(c, props)

def isBidiControl(c: int) -> bool:
    props = bidiPropsTrie.get(c)
    return getFlagFromProps(props, UBIDI_BIDI_CONTROL_SHIFT)

def isJoinControl(c: int) -> bool:
    props = bidiPropsTrie.get(c)
    return getFlagFromProps(props, UBIDI_JOIN_CONTROL_SHIFT)

def getJoiningType(c: int) -> int:
    props = bidiPropsTrie.get(c)
    return (props & UBIDI_JT_MASK) >> UBIDI_JT_SHIFT

def getJoiningGroup(c: int) -> int:
    start = ubidi_props_indexes[UBIDI_IX_JG_START]
    limit = ubidi_props_indexes[UBIDI_IX_JG_LIMIT]

    if c in range(start, limit):
        return ubidi_props_jgArray[c - start]

    start = ubidi_props_indexes[UBIDI_IX_JG_START2]
    limit = ubidi_props_indexes[UBIDI_IX_JG_LIMIT2]

    if c in range(start, limit):
        return ubidi_props_jgArray2[c - start]

    return U_JG_NO_JOINING_GROUP

def getPairedBracketType(c: int) -> int:
    props = bidiPropsTrie.get(c)
    return (props & UBIDI_BPT_MASK) >> UBIDI_BPT_SHIFT

def getPairedBracket(c: int) -> int:
    props = bidiPropsTrie.get(c)
    if (props & UBIDI_BPT_MASK) == 0:
        return c

    return getMirrorFromProps(c, props)

