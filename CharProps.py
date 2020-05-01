
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
        return ntv - UPROPS_NTV_DECIMAL_START

    if ntv < UPROPS_NTV_NUMERIC_START:
        return ntv - UPROPS_NTV_DIGIT_START

    if ntv < UPROPS_NTV_FRACTION_START:
        return ntv - UPROPS_NTV_NUMERIC_START

    if ntv < UPROPS_NTV_LARGE_START:
        numerator = (ntv >> 4) - 12
        denominator = (ntv & 0xf) + 1
        return numerator / denominator

    # need to finish this...
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
print(f"getNumericValue(0x0037) = {getNumericValue(0x37)}")
print(f"getNumericValue(0x00BE) = {getNumericValue(0x00BE)}")
print(f"getNumericValue(0x0969) = {getNumericValue(0x0969)}")
print(f"getAge(0x0220) = {getAge(0x0220)}")