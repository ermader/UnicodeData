"""\
Based on ucase.h, ucase_props.cpp from ICU

Created on May 8, 2020

@author Eric Mader
"""

from CasePropsData import *
from Utrie2 import UTrie2

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

# We want an arithmetic shift. There's got to be a better way to do this...
# This should be in a utilities module...
def arithmeticShift(value, bitsInWord, bitsInField):
    signBit = 1 << (bitsInWord - 1)
    shift = bitsInWord - bitsInField
    result = value >> shift

    return result - (1 << bitsInField) if (value & signBit) != 0 else result

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
    if (excWord & UCASE_EXC_DOUBLE_SLOTS) == 0:
        exceptionIndex += slotOffset(excWord, index)
        return ucase_props_exceptions[exceptionIndex]

    exceptionIndex += 2 * slotOffset(excWord, index)
    return (ucase_props_exceptions[exceptionIndex]) << 16 | ucase_props_exceptions[exceptionIndex+1]

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
            delta = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex)
            return c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta

        if hasSlot(excWord, UCASE_EXC_LOWER):
            c = getSlotValue(excWord, UCASE_EXC_LOWER, exceptionIndex)

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
            delta = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex)
            return c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta

        if hasSlot(excWord, UCASE_EXC_UPPER):
            c = getSlotValue(excWord, UCASE_EXC_UPPER, exceptionIndex)

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
            delta = getSlotValue(excWord, UCASE_EXC_DELTA, exceptionIndex)
            return c + delta if (excWord & UCASE_EXC_DELTA_IS_NEGATIVE) == 0 else c - delta

        for slot in [UCASE_EXC_TITLE, UCASE_EXC_UPPER]:
            if hasSlot(excWord, slot):
                return getSlotValue(excWord, slot, exceptionIndex)

    return c

casePropsTrie = UTrie2(ucase_props_trieIndex, ucase_props_trie_index_length, ucase_props_trie_index_2_null_offset, \
                       ucase_props_trie_data_null_offset, ucase_props_trie_high_start, ucase_props_trie_high_value_index)

def test():
    print(f"toLower('A') is '{chr(toLower(ord('A')))}'")
    print(f"toLower('a') is '{chr(toLower(ord('a')))}'")
    print(f"toLower('{chr(0x0130)}') is '{chr(toLower(0x0130))}'")
    print(f"toLower('{chr(0x0131)}') is '{chr(toLower(0x0131))}'")
    print(f"toLower('Г') is '{chr(toLower(ord('Г')))}'")
    print(f"toLower('г') is '{chr(toLower(ord('г')))}'")
    print()

    print(f"toUpper('A') is '{chr(toUpper(ord('A')))}'")
    print(f"toUpper('a') is '{chr(toUpper(ord('a')))}'")
    print(f"toUpper('{chr(0x0130)}') is '{chr(toUpper(0x0130))}'")
    print(f"toUpper('{chr(0x0131)}') is '{chr(toUpper(0x0131))}'")
    print(f"toUpper('Г') is '{chr(toUpper(ord('Г')))}'")
    print(f"toUpper('г') is '{chr(toUpper(ord('г')))}'")
    print()

    print(f"toTitle('A') is '{chr(toTitle(ord('A')))}'")
    print(f"toTitle('a') is '{chr(toTitle(ord('a')))}'")
    print(f"toTitle('K') is '{chr(toTitle(ord('K')))}'")
    print(f"toTitle('{chr(0x0130)}') is '{chr(toTitle(0x0130))}'")
    print(f"toTitle('{chr(0x0131)}') is '{chr(toTitle(0x0131))}'")
    print(f"toTitle('Г') is '{chr(toTitle(ord('Г')))}'")
    print(f"toTitle('г') is '{chr(toTitle(ord('г')))}'")



if __name__ == "__main__":
    test()