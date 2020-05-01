
from Utrie2 import UTrie2
from CharPropsData import propsTrie_index, propsTrie_index_length, propsTrie_index_2_null_offset, propsTrie_data_null_offset, \
    propsTrie_high_start, propsTrie_high_value_index, \
    propsVectorsTrie_index, propsVectorsTrie_index_length, propsVectorsTrie_index_2_null_offset, propsVectorsTrie_data_null_offset, \
    propsVectorsTrie_high_start, propsVectorTrie_high_value_index, propsVectors, propsVectorColumns, scriptExtensions
from Scripts import *


propsTrie = UTrie2(propsTrie_index, propsTrie_index_length, propsTrie_index_2_null_offset, propsTrie_data_null_offset, \
                   propsTrie_high_start, propsTrie_high_value_index)

propsVectorTrie = UTrie2(propsVectorsTrie_index, propsVectorsTrie_index_length, propsVectorsTrie_index_2_null_offset, propsVectorsTrie_data_null_offset, \
                         propsVectorsTrie_high_start, propsVectorTrie_high_value_index)


def getUnicodeProperties(c, column):
    if column > propsVectorColumns:
        return 0

    vecIndex = propsVectorTrie.get(c)
    return propsVectors[vecIndex+column]

UPROPS_CATEGORY_MASK = 0x1F
UPROPS_NUMERIC_TYPE_VALUE_SHIFT = 6

UPROPS_NTV_NONE = 0  # no numeric value
UPROPS_NTV_DECIMAL_START = 1  # Decimal digits 0 - 9
UPROPS_NTV_DIGIT_START = 11  # Other digits
UPROPS_NTV_NUMERIC_START = 21  # Small integers nv = 0..154
UPROPS_NTV_FRACTION_START = 0xb0  # Fractions: ((ntv>>4)-12) / ((ntv&0xf)+1) = -1..17 / 1..16
UPROPS_NTV_LARGE_START = 0x1e0  # Large integers: ((ntv>>5)-14) * 10^((ntv&0x1f)+2) = (1..9)*(10^2..10^33)
UPROPS_NTV_BASE60_START = 0x300  # Sexagesimal numbers: ((ntv>>2)-0xbf) * 60^((ntv&3)+1) = (1..9)*(60^1..60^4)
UPROPS_NTV_FRACTION20_START = UPROPS_NTV_BASE60_START + 36  #
UPROPS_NTV_FRACTION32_START = UPROPS_NTV_FRACTION20_START + 24
UPROPS_NTV_RESERVED_START = UPROPS_NTV_FRACTION32_START + 16

def getNumericType(c):
    props = propsTrie.get(c)
    return props & UPROPS_CATEGORY_MASK

def getNumericTypeValue(c):
    props = propsTrie.get(c)
    return props >> UPROPS_NUMERIC_TYPE_VALUE_SHIFT

def getNumericValue(c):
    ntv = getNumericTypeValue(c)

    if ntv == UPROPS_NTV_NONE:
        return None

    if ntv < UPROPS_NTV_DIGIT_START:
        # decimal digit
        return ntv - UPROPS_NTV_DECIMAL_START

    if ntv < UPROPS_NTV_NUMERIC_START:
        # other digit
        return ntv - UPROPS_NTV_DIGIT_START

    if ntv < UPROPS_NTV_FRACTION_START:
        # small integer
        return ntv - UPROPS_NTV_NUMERIC_START

    if ntv < UPROPS_NTV_LARGE_START:
        # fraction
        numerator = (ntv >> 4) - 12
        denominator = (ntv & 0xf) + 1
        return numerator / denominator

    if ntv < UPROPS_NTV_BASE60_START:
        # large, single-significant-digit integer
        mant = (ntv >> 5) - 14
        exp = (ntv & 0x1f) + 2
        numValue = mant

        # multiply by 10^exp without math.h
        while exp >= 4:
            numValue *= 10000.0
            exp -= 4

        if exp == 3:
            numValue *= 1000.0
        elif exp == 2:
            numValue *= 100.0
        elif exp == 1:
            numValue *= 10.0

        return numValue

    if ntv < UPROPS_NTV_FRACTION20_START:
        # sexagesimal (base 60) integer
        numValue = (ntv >> 2) - 0xbf
        exp = (ntv & 3) + 1

        if exp == 4:
            numValue *= 60*60*60*60
        elif exp == 3:
            numValue *= 60*60*60
        elif exp == 2:
            numValue *= 60*60
        elif exp == 1:
            numValue *= 60

        return numValue

    if ntv < UPROPS_NTV_FRACTION32_START:
        # fraction-20 e.g. 3/80
        frac20 = ntv-UPROPS_NTV_FRACTION20_START  # 0..0x17
        numerator = 2 * (frac20 & 3) + 1
        denominator = 20 << (frac20 >> 2)

        return numerator/denominator

    if ntv < UPROPS_NTV_RESERVED_START:
        # fraction-32 e.g. 3/64
        frac32 = ntv-UPROPS_NTV_FRACTION32_START  # 0..15
        numerator = 2 * (frac32 & 3) + 1
        denominator = 32 << (frac32 >> 2)

        return numerator/denominator

    return None

# Probably want to move these to a uprops class...
# derived age: one nibble each for major and minor version numbers
UPROPS_AGE_MASK = 0xff000000
UPROPS_AGE_SHIFT = 24

# Script_Extensions: mask includes Script
UPROPS_SCRIPT_X_MASK = 0x00f000ff
UPROPS_SCRIPT_X_SHIFT = 22

# The UScriptCode or Script_Extensions index is split across two bit fields.
# (Starting with Unicode 13/ICU 66/2019 due to more varied Script_Extensions.)
# Shift the high bits right by 12 to assemble the full value.
UPROPS_SCRIPT_HIGH_MASK  = 0x00300000
UPROPS_SCRIPT_HIGH_SHIFT = 12
UPROPS_MAX_SCRIPT = 0x3ff

UPROPS_EA_MASK = 0x000e0000
UPROPS_EA_SHIFT = 7

UPROPS_BLOCK_MASK = 0x0001ff00
UPROPS_BLOCK_SHIFT = 8

UPROPS_SCRIPT_LOW_MASK = 0x000000ff

# UPROPS_SCRIPT_X_WITH_COMMON must be the lowest value that involves Script_Extensions.
UPROPS_SCRIPT_X_WITH_COMMON = 0x400000
UPROPS_SCRIPT_X_WITH_INHERITED = 0x800000
UPROPS_SCRIPT_X_WITH_OTHER = 0xc00000

def getAge(c):
    age = getUnicodeProperties(c, 0) >> UPROPS_AGE_SHIFT
    return [age >> 4, age & 0xF, 0, 0]

def mergeScriptCodeOrIndex(scriptX):
    return \
        ((scriptX & UPROPS_SCRIPT_HIGH_MASK) >> UPROPS_SCRIPT_HIGH_SHIFT) | \
        (scriptX & UPROPS_SCRIPT_LOW_MASK)

def getScript(c):
    if c > 0x10FFFF:
        return USCRIPT_INVALID_CODE

    scriptX = getUnicodeProperties(c, 0) & UPROPS_SCRIPT_X_MASK
    codeOrIndex = mergeScriptCodeOrIndex(scriptX)

    if scriptX < UPROPS_SCRIPT_X_WITH_COMMON:
        return codeOrIndex

    if scriptX < UPROPS_SCRIPT_X_WITH_INHERITED:
        return USCRIPT_COMMON

    if scriptX < UPROPS_SCRIPT_X_WITH_OTHER:
        return USCRIPT_INHERITED

    return scriptExtensions[codeOrIndex]

print(f"getScript(0x0915) = '{scriptCodes[getScript(0x0915)]}'")
print(f"getScript(0x1E900) = '{scriptCodes[getScript(0x1E900)]}'")
print(f"getNumericValue(0x0037) = {getNumericValue(0x37)}")  # DIGIT SEVEN
print(f"getNumericValue(0x00BE) = {getNumericValue(0x00BE)}")  # VULGAR FRACTION THREE QUARTERS
print(f"getNumericValue(0x09F6) = {getNumericValue(0x09F6)}")  # BENGALI CURRENCY NUMERATOR THREE (3/16)
print(f"getNumericValue(0x0BF1) = {getNumericValue(0x0BF1)}")  # TAMIL NUMBER ONE HUNDRED
print(f"getNumericValue(0x1ED2D) = {getNumericValue(0x1ED2D)}")  # OTTOMAN SIYAQ NUMBER NINETY THOUSAND
print(f"getAge(0x0220) = {getAge(0x0220)}")