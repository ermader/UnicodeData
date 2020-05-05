
from Utrie2 import UTrie2
from CharPropsData import *
from Scripts import *
from GeneralCategories import *
from Characters import *


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

def getGeneralCategory(c):
    props = propsTrie.get(c)
    return props & 0x1F

def gcMask(gc):
    return 1 << gc

def isLower(c):
    return getGeneralCategory(c) == GC_LOWERCASE_LETTER

def isUpper(c):
    return getGeneralCategory(c) == GC_UPPERCASE_LETTER

def isTitle(c):
    return getGeneralCategory(c) == GC_TITLECASE_LETTER

def isDigit(c):
    return getGeneralCategory(c) == GC_DECIMAL_DIGIT_NUMBER

def isHexDigit(c):
    if c in range(CH_U_A, CH_U_F + 1) or c in range(CH_U_a, CH_U_f + 1):
        return True

    if c in range(CH_U_FW_A, CH_U_FW_F + 1) or c in range(CH_U_FW_a, CH_U_FW_f + 1):
        return True

    return isDigit(c)

def isalpha(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & GC_L_MASK) != 0

def isAlphabetic(c):
    props = getUnicodeProperties(c, 1)
    return (props & (1 << UPROPS_ALPHABETIC)) != 0

def isalnum(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & (GC_L_MASK | GC_ND_MASK)) != 0

def isalnumPOSIX(c):
    return isAlphabetic(c) or isDigit(c)

def isDefined(c):
    return getGeneralCategory(c) != GC_UNASSIGNED

def isbase(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & (GC_L_MASK | GC_N_MASK | GC_MC_MASK | GC_ME_MASK)) != 0

def iscntrl(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & (GC_CC_MASK | GC_CF_MASK | GC_ZL_MASK | GC_ZP_MASK)) != 0

def isISOControl(c):
    return c <= 0x001F or c in range(0x007F, 0x009F+1)

def isThatControlSpace(c):
    # Some control characters that are used as space.
    return c <= 0x9f and ((c >= CH_TAB and c <= CH_CR) or (c >= 0x1c and c <= 0x1f) or c == CH_NL)

def isThatASCIIControlSpace(c):
    # Java has decided  that U+0085 New Line is not whitespace any more.
    return c <= 0x1f and c >= CH_TAB and (c <= CH_CR or c>=0x1c)

def isspace(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & GC_Z_MASK) != 0 or isThatControlSpace(c)

def isJavaSpaceChar(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & GC_Z_MASK) != 0

def isWhiteSpace(c):
    if c == CH_NBSP or c == CH_FIGURESP or c == CH_NNBSP:
        return False

    gc = getGeneralCategory(c)
    return (gcMask(gc) & GC_Z_MASK) != 0 or isThatASCIIControlSpace(c)

def isBlank(c):
    if c <= 0x009F:
        return c == CH_TAB or c == CH_SPACE

    gc = getGeneralCategory(c)
    return gc == GC_SPACE_SEPARATOR

def isUWhiteSpace(c):
    props = getUnicodeProperties(c, 1)
    return (props & (1 << UPROPS_WHITE_SPACE)) != 0

def isPrint(c):
    gc = getGeneralCategory(c)
    # comparing == 0 returns False for the categories mentioned
    return (gcMask(gc) & GC_C_MASK) == 0

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
# Values in vector word 0
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
UPROPS_EA_SHIFT = 17

UPROPS_BLOCK_MASK = 0x0001ff00
UPROPS_BLOCK_SHIFT = 8

UPROPS_SCRIPT_LOW_MASK = 0x000000ff

# UPROPS_SCRIPT_X_WITH_COMMON must be the lowest value that involves Script_Extensions.
UPROPS_SCRIPT_X_WITH_COMMON = 0x400000
UPROPS_SCRIPT_X_WITH_INHERITED = 0x800000
UPROPS_SCRIPT_X_WITH_OTHER = 0xc00000

# Flags in vector word 1
UPROPS_WHITE_SPACE = 0
UPROPS_DASH = 1
UPROPS_HYPHEN = 2
UPROPS_QUOTATION_MARK = 3
UPROPS_TERMINAL_PUNCTUATION = 4
UPROPS_MATH = 5
UPROPS_HEX_DIGIT = 6
UPROPS_ASCII_HEX_DIGIT = 7
UPROPS_ALPHABETIC = 8
UPROPS_IDEOGRAPHIC = 9
UPROPS_DIACRITIC = 10
UPROPS_EXTENDER = 11
UPROPS_NONCHARACTER_CODE_POINT = 12
UPROPS_GRAPHEME_EXTEND = 13
UPROPS_GRAPHEME_LINK = 14
UPROPS_IDS_BINARY_OPERATOR = 15
UPROPS_IDS_TRINARY_OPERATOR = 16
UPROPS_RADICAL = 17
UPROPS_UNIFIED_IDEOGRAPH = 18
UPROPS_DEFAULT_IGNORABLE_CODE_POINT = 19
UPROPS_DEPRECATED = 20
UPROPS_LOGICAL_ORDER_EXCEPTION = 21
UPROPS_XID_START = 22
UPROPS_XID_CONTINUE = 23
UPROPS_ID_START = 24                            #  ICU 2.6, uprops format version 3.2
UPROPS_ID_CONTINUE = 25
UPROPS_GRAPHEME_BASE = 26
UPROPS_S_TERM = 27                              #  new in ICU 3.0 and Unicode 4.0.1
UPROPS_VARIATION_SELECTOR = 28
UPROPS_PATTERN_SYNTAX = 29                      #  new in ICU 3.4 and Unicode 4.1
UPROPS_PATTERN_WHITE_SPACE = 30
UPROPS_PREPENDED_CONCATENATION_MARK = 31            # new in ICU 60 and Unicode 10
UPROPS_BINARY_1_TOP = 32                        #  ==32 - full!

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

def getBlock(c):
    props = getUnicodeProperties(c, 0)
    return (props & UPROPS_BLOCK_MASK) >> UPROPS_BLOCK_SHIFT

def getEastAsianWidth(c):
    props = getUnicodeProperties(c, 0)
    return (props & UPROPS_EA_MASK) >> UPROPS_EA_SHIFT

def test():
    print(f"General Category of U+0012 is {generalCategories[getGeneralCategory(0x0012)]}")
    print(f"General Category of '3' is {generalCategories[getGeneralCategory(ord('3'))]}")
    print(f"General Category of '(' is {generalCategories[getGeneralCategory(ord('('))]}")
    print(f"General Category of ')' is {generalCategories[getGeneralCategory(ord(')'))]}")
    print(f"General Category of 'A' is {generalCategories[getGeneralCategory(ord('A'))]}")
    print(f"General Category of 'a' is {generalCategories[getGeneralCategory(ord('a'))]}")
    print(f"General Category of '{chr(0x0644)}' is {generalCategories[getGeneralCategory(0x0644)]}")
    print(f"General Category of '{chr(0x0915)}' is {generalCategories[getGeneralCategory(0x0915)]}")
    print(f"General Category of '{chr(0x3010)}' is {generalCategories[getGeneralCategory(0x3010)]}")
    print(f"General Category of '{chr(0x3011)}' is {generalCategories[getGeneralCategory(0x3011)]}")
    print()

    print(f"Script of '{chr(0x0915)}' is '{scriptCodes[getScript(0x0915)]}'")
    print(f"Script of U+1E900 is '{scriptCodes[getScript(0x1E900)]}'")
    print()

    print(f"Numeric value of '7' is {getNumericValue(ord('7'))}")  # DIGIT SEVEN
    print(f"Numeric value of '{chr(0x00BE)}' is {getNumericValue(0x00BE)}")  # VULGAR FRACTION THREE QUARTERS
    print(f"Numeric value of '{chr(0x0667)}' is {getNumericValue(0x0667)}")  # ARABIC-INDIC DIGIT SEVEN
    print(f"Numeric value of '{chr(0x09F6)}' is {getNumericValue(0x09F6)}")  # BENGALI CURRENCY NUMERATOR THREE (3/16)
    print(f"Numeric value of '{chr(0x0BF1)}' is {getNumericValue(0x0BF1)}")  # TAMIL NUMBER ONE HUNDRED
    print(f"Numeric value of U+0x1ED2D is {getNumericValue(0x1ED2D)}")  # OTTOMAN SIYAQ NUMBER NINETY THOUSAND
    print()

    print(f"Age of '{chr(0x0220)}' is {getAge(0x0220)}")
    print(f"'a' is alphabetic: {isAlphabetic(ord('a'))}")

if __name__ == "__main__":
    test()