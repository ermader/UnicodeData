"""\
Based on ucase.h, ucase_props.cpp from ICU

Created on May 8, 2020

@author Eric Mader
"""

from .CasePropsData import *
from .Utrie2 import UTrie2
from .Utilities import arithmeticShift

# Indexes into ucase_props_indexes
UCASE_IX_INDEX_TOP = 0
UCASE_IX_LENGTH = 1
UCASE_IX_TRIE_SIZE = 2
UCASE_IX_EXC_LENGTH = 3
UCASE_IX_UNFOLD_LENGTH = 4

UCASE_IX_MAX_FULL_LENGTH = 15
UCASE_IX_TOP = 16

# 2-bit constants for types of cased characters
UCASE_TYPE_MASK = 3
UCASE_NONE = 0
UCASE_LOWER = 1
UCASE_UPPER = 2
UCASE_TITLE = 3

UCASE_IGNORABLE = 4
UCASE_EXCEPTION = 8
UCASE_SENSITIVE = 0x10

UCASE_DOT_MASK = 0x60
UCASE_NO_DOT=0         # normal characters with cc=0
UCASE_SOFT_DOTTED=0x20 # soft-dotted characters with cc=0
UCASE_ABOVE=0x40       # "above" accents with cc=230
UCASE_OTHER_ACCENT=0x60 # other accent character (0<cc!=230)

UCASE_PROPS_BITS = 16
# no exception: bits 15..7 are a 9-bit signed case mapping delta
UCASE_DELTA_BITS = 9
UCASE_DELTA_SHIFT = 7
UCASE_DELTA_MASK = 0xff80
UCASE_MAX_DELTA = 0xff
UCASE_MIN_DELTA = (-UCASE_MAX_DELTA-1)

# exception: bits 15..4 are an unsigned 12-bit index into the exceptions array
UCASE_EXC_SHIFT = 4
UCASE_EXC_MASK = 0xfff0
UCASE_MAX_EXCEPTIONS = ((UCASE_EXC_MASK >> UCASE_EXC_SHIFT) + 1)

# definitions for 16-bit main exceptions word

# first 8 bits indicate values in optional slots
UCASE_EXC_LOWER = 0
UCASE_EXC_FOLD = 1
UCASE_EXC_UPPER = 2
UCASE_EXC_TITLE = 3
UCASE_EXC_DELTA = 4
UCASE_EXC_5 = 5  # reserved
UCASE_EXC_CLOSURE = 6
UCASE_EXC_FULL_MAPPINGS = 7
UCASE_EXC_ALL_SLOTS  = 8 # one past the last slot

# each slot is 2 uint16_t instead of 1
UCASE_EXC_DOUBLE_SLOTS = 0x100

UCASE_EXC_NO_SIMPLE_CASE_FOLDING = 0x200
UCASE_EXC_DELTA_IS_NEGATIVE = 0x400
UCASE_EXC_SENSITIVE = 0x800

UCASE_EXC_DOT_SHIFT = 7
UCASE_EXC_DOT_MASK  = UCASE_DOT_MASK << UCASE_EXC_DOT_SHIFT

# normally stored in the main word, but pushed out for larger exception indexes
UCASE_EXC_NO_DOT = 0
UCASE_EXC_SOFT_DOTTED = 0x1000
UCASE_EXC_ABOVE = 0x2000   # "above" accents with cc=230
UCASE_EXC_OTHER_ACCENT = 0x3000 # other character(0 < cc != 230)

# complex/conditional mappings
UCASE_EXC_CONDITIONAL_SPECIAL = 0x4000
UCASE_EXC_CONDITIONAL_FOLD = 0x8000

# definitions for lengths word for full case mappings
UCASE_FULL_LOWER = 0xf
UCASE_FULL_FOLDING = 0xf0
UCASE_FULL_UPPER = 0xf00
UCASE_FULL_TITLE = 0xf000

# maximum lengths
UCASE_FULL_MAPPINGS_MAX_LENGTH = 4 * 0xf
UCASE_CLOSURE_MAX_LENGTH = 0xf

# constants for reverse case folding ("unfold") data
UCASE_UNFOLD_ROWS = 0
UCASE_UNFOLD_ROW_WIDTH = 1
UCASE_UNFOLD_STRING_WIDTH = 2

flagsOffset = [
    0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
]

def getDeltaFromProps(props):
    return arithmeticShift(props, UCASE_PROPS_BITS, UCASE_DELTA_BITS)

def getTypeFromProps(props):
    return props & UCASE_TYPE_MASK

def getTypeAndIgnorableFromProps(props):
    return props & (UCASE_TYPE_MASK | UCASE_IGNORABLE)

def isUpperOrTitle(props):
    return (props & (UCASE_UPPER & UCASE_TITLE)) != 0

def hasException(props):
    return (props & UCASE_EXCEPTION) != 0

def hasSlot(flags, index):
    return (flags & (1 << index)) != 0

def slotOffset(flags, index):
    return flagsOffset[flags & ((1 << index) - 1)]

def getSlotValue(excWord, index, exceptionIndex):
    slot_offset = slotOffset(excWord, index)
    if (excWord & UCASE_EXC_DOUBLE_SLOTS) == 0:
        exceptionIndex += slot_offset
        return (ucase_props_exceptions[exceptionIndex], slot_offset)

    exceptionIndex += 2 * slot_offset
    return ((ucase_props_exceptions[exceptionIndex]) << 16 | ucase_props_exceptions[exceptionIndex+1], (2 * slot_offset) + 1)

def toLower(c):
    props = casePropsTrie.get(c)

    if not hasException(props):
        if isUpperOrTitle(props):
            c += getDeltaFromProps(props)
    else:
        # handle exceptions
        exceptionIndex = props >> UCASE_EXC_SHIFT
        excWord = ucase_props_exceptions[exceptionIndex]
        exceptionIndex += 1
        if hasSlot(excWord, UCASE_EXC_DELTA) and isUpperOrTitle(props):
            (delta, _) = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex)
            return c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta

        if hasSlot(excWord, UCASE_EXC_LOWER):
            (c, _) = getSlotValue(excWord, UCASE_EXC_LOWER, exceptionIndex)

    return c

def toUpper(c):
    props = casePropsTrie.get(c)

    if not hasException(props):
        if getTypeFromProps(props) == UCASE_LOWER:
            c += getDeltaFromProps(props)
    else:
        exceptionIndex = props >> UCASE_EXC_SHIFT
        excWord = ucase_props_exceptions[exceptionIndex]
        exceptionIndex += 1
        if hasSlot(excWord, UCASE_EXC_DELTA) and getTypeFromProps(props) == UCASE_LOWER:
            (delta, _) = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex)
            return c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta

        if hasSlot(excWord, UCASE_EXC_UPPER):
            (c, _) = getSlotValue(excWord, UCASE_EXC_UPPER, exceptionIndex)

    return c

def toTitle(c):
    props = casePropsTrie.get(c)

    if not hasException(props):
        if getTypeFromProps(props) == UCASE_LOWER:
            c += getDeltaFromProps(props)
    else:
        exceptionIndex = props >> UCASE_EXC_SHIFT
        excWord = ucase_props_exceptions[exceptionIndex]
        exceptionIndex += 1
        if hasSlot(excWord, UCASE_EXC_DELTA) and getTypeFromProps(props) == UCASE_LOWER:
            (delta, _) = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex)
            return c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta

        for slot in [UCASE_EXC_TITLE, UCASE_EXC_UPPER]:
            if hasSlot(excWord, slot):
                return getSlotValue(excWord, slot, exceptionIndex)[0]

    return c

# locale?
def toFullLower(c):
    result = chr(c)
    props = casePropsTrie.get(c)

    if not hasException(props):
        if isUpperOrTitle(props):
            return chr(c + getDeltaFromProps(props))
    else:
        exceptionIndex = props >> UCASE_EXC_SHIFT
        excWord = ucase_props_exceptions[exceptionIndex]
        exceptionIndex += 1
        exceptionIndex2 = exceptionIndex

        if (excWord & UCASE_EXC_CONDITIONAL_SPECIAL) != 0:
            # this is were to handle locale exceptions
            if c == 0x0130:  # Upper case dotted I
                return "i\u0307"
        elif hasSlot(excWord, UCASE_EXC_FULL_MAPPINGS):
            (full, offset) = getSlotValue(excWord, UCASE_EXC_FULL_MAPPINGS, exceptionIndex)
            full &= UCASE_FULL_LOWER
            if full != 0:
                chars = []
                exceptionIndex += offset + 1
                for i in range(full):
                    chars.append(chr(ucase_props_exceptions[exceptionIndex + i]))

                return "".join(chars)

        if hasSlot(excWord, UCASE_EXC_DELTA) and isUpperOrTitle(props):
            (delta, _) = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex2)
            return chr(c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta)

        if hasSlot(excWord, UCASE_EXC_LOWER):
            (ch, _) = getSlotValue(excWord, UCASE_EXC_LOWER, exceptionIndex2)
            return chr(ch)

    return result

# locale?
def toUpperOrTitle(c, upperNotTitle):
    result = chr(c)
    props = casePropsTrie.get(c)

    if not hasException(props):
        if getTypeFromProps(props) == UCASE_LOWER:
            result = chr(c + getDeltaFromProps(props))
    else:
        exceptionIndex = props >> UCASE_EXC_SHIFT
        excWord = ucase_props_exceptions[exceptionIndex]
        exceptionIndex += 1
        exceptionIndex2 = exceptionIndex

        if (excWord & UCASE_EXC_CONDITIONAL_SPECIAL) != 0:
            # this is where to handle locale exceptions...
            if c == 0x0587:
                # See ICU-13416:
                # և ligature ech-yiwn
                # uppercases to ԵՒ=ech+yiwn by default and in Western Armenian,
                # but to ԵՎ=ech+vew in Eastern Armenian.
                return "ԵՒ" if upperNotTitle else "Եւ"

        elif hasSlot(excWord, UCASE_EXC_FULL_MAPPINGS):
            (full, offset) = getSlotValue(excWord, UCASE_EXC_FULL_MAPPINGS, exceptionIndex)
            exceptionIndex += offset + 1 + (full & UCASE_FULL_LOWER)
            full >>= 4
            exceptionIndex += full & 0xF
            full >>= 4

            if upperNotTitle:
                full &= 0xF
            else:
                exceptionIndex += full &0xF
                full = (full >> 4) & 0xF

            if full != 0:
                chars = []
                for i in range(full):
                    chars.append(chr(ucase_props_exceptions[exceptionIndex + i]))

                return "".join(chars)

        if hasSlot(excWord, UCASE_EXC_DELTA) and getTypeFromProps(props) == UCASE_LOWER:
            (delta, _) = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex2)
            return chr(c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta)

        if (not upperNotTitle) and hasSlot(excWord, UCASE_EXC_TITLE):
            idx = UCASE_EXC_TITLE
        elif hasSlot(excWord, UCASE_EXC_UPPER):
            idx = UCASE_EXC_UPPER
        else:
            return result

        (ch, _) = getSlotValue(excWord, idx, exceptionIndex2)
        return chr(ch)

    return result

def toFullUpper(c):
    return toUpperOrTitle(c, True)

def toFullTitle(c):
    return toUpperOrTitle(c, False)

casePropsTrie = UTrie2(ucase_props_trieIndex, ucase_props_trie_index_length, ucase_props_trie_index_2_null_offset, \
                       ucase_props_trie_data_null_offset, ucase_props_trie_high_start, ucase_props_trie_high_value_index)
