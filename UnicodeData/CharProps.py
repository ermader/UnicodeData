
from .Utrie2 import UTrie2
from .CharPropsData import *
from .uprops_h import *
from .uscript_h import *
from .UCDTypeDictionaries import generalCategoryNames as generalCategories
from .UCDTypeDictionaries import scriptNames as scriptCodes
from .UCDTypeDictionaries import blockNames
from .Characters import *
from .GeneralCategories import *
from UnicodeData import EnumeratorTests

propsTrie = UTrie2(propsTrie_index, propsTrie_index_length, propsTrie_index_2_null_offset, propsTrie_data_null_offset, \
                   propsTrie_high_start, propsTrie_high_value_index)

propsVectorTrie = UTrie2(propsVectorsTrie_index, propsVectorsTrie_index_length, propsVectorsTrie_index_2_null_offset, propsVectorsTrie_data_null_offset, \
                         propsVectorsTrie_high_start, propsVectorsTrie_high_value_index)

def unicodePropertiesFromVecIndex(vecIndex, column):
    return propsVectors[vecIndex + column]

def getUnicodeProperties(c, column):
    if column > propsVectorsColumns:
        return 0

    vecIndex = propsVectorTrie.get(c)
    return unicodePropertiesFromVecIndex(vecIndex, column)

def generalCategoryFromProps(props):
    return props & 0x1F

def getGeneralCategory(c):
    props = propsTrie.get(c)
    return generalCategoryFromProps(props)

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

def isPrintPOSIX(c):
    gc = getGeneralCategory(c)
    return gc == GC_SPACE_SEPARATOR or isGraphPOSIX(c)

def isgraph(c):
    gc = getGeneralCategory(c)
    # comparing == 0 returns False for the categories mentioned
    return (gcMask(gc) & (GC_CC_MASK | GC_CF_MASK | GC_CS_MASK | GC_CN_MASK | GC_Z_MASK)) == 0

def isGraphPOSIX(c):
    gc = getGeneralCategory(c)
    # comparing == 0 returns False for the categories mentioned
    return (gcMask(gc) & (GC_CC_MASK | GC_CS_MASK | GC_CN_MASK | GC_Z_MASK)) == 0

def ispunct(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & GC_P_MASK) != 0

def isIDStart(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & ( GC_L_MASK | GC_NL_MASK)) != 0

def isIDPart(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & ( GC_ND_MASK | GC_NL_MASK | GC_L_MASK | GC_PC_MASK | GC_MC_MASK | GC_MN_MASK)) != 0 or isIDIgnorable(c)

def isIDIgnorable(c):
    if c < 0x009F:
        isISOControl(c) and not isThatASCIIControlSpace(c)

    gc = getGeneralCategory(c)
    return gc == GC_FORMAT_CHAR

def isJavaIDStart(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & (GC_L_MASK | GC_SC_MASK | GC_PC_MASK)) != 0

def isJavaIDPart(c):
    gc = getGeneralCategory(c)
    return (gcMask(gc) & (GC_ND_MASK | GC_NL_MASK | GC_L_MASK | GC_SC_MASK | GC_PC_MASK |GC_MC_MASK | GC_MN_MASK)) != 0 or isIDIgnorable(c)

def digitValue(c):
    props = propsTrie.get(c)
    value = getNumericTypeValue(c) - UPROPS_NTV_DECIMAL_START
    return value if value <= 9 else -1

def numericTypeFromProps(props):
    return props & 0x1F

def getNumericType(c):
    props = propsTrie.get(c)
    return numericTypeFromProps(props)

def numericTypeValueFromProps(props):
    return props >> UPROPS_NUMERIC_TYPE_VALUE_SHIFT

def getNumericTypeValue(c):
    props = propsTrie.get(c)
    return props >> UPROPS_NUMERIC_TYPE_VALUE_SHIFT

def numericValueFromProps(props):
    ntv = numericTypeValueFromProps(props)

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

def getNumericValue(c):
    props = propsTrie.get(c)
    return numericValueFromProps(props)

def ageFromProps(props):
    age = props >> UPROPS_AGE_SHIFT
    return [age >> 4, age & 0xF, 0, 0]

def getAge(c):
    props = getUnicodeProperties(c, 0)
    return ageFromProps(props)

def mergeScriptCodeOrIndex(scriptX):
    return \
        ((scriptX & UPROPS_SCRIPT_HIGH_MASK) >> UPROPS_SCRIPT_HIGH_SHIFT) | \
        (scriptX & UPROPS_SCRIPT_LOW_MASK)

def scriptFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 0)
    scriptX = props & UPROPS_SCRIPT_X_MASK
    codeOrIndex = mergeScriptCodeOrIndex(scriptX)

    if scriptX < UPROPS_SCRIPT_X_WITH_COMMON:
        return codeOrIndex

    if scriptX < UPROPS_SCRIPT_X_WITH_INHERITED:
        return USCRIPT_COMMON

    if scriptX < UPROPS_SCRIPT_X_WITH_OTHER:
        return USCRIPT_INHERITED

    return scriptExtensions[codeOrIndex]

def getScript(c):
    if c > 0x10FFFF:
        return USCRIPT_INVALID_CODE

    vecIndex = propsVectorTrie.get(c)

    return scriptFromVecIndex(vecIndex)

def blockFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 0)
    return (props & UPROPS_BLOCK_MASK) >> UPROPS_BLOCK_SHIFT

def getBlock(c):
    vecIndex = propsVectorTrie.get(c)
    return blockFromVecIndex(vecIndex)

def eastAsianWidthFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 0)

    return (props & UPROPS_EA_MASK) >> UPROPS_EA_SHIFT

def getEastAsianWidth(c):
    vecIndex = propsVectorTrie.get(c)
    return eastAsianWidthFromVecIndex(vecIndex)

def lineBreakFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 2)
    return (props & UPROPS_LB_MASK) >> UPROPS_LB_SHIFT

def getLineBreak(c):
    vecIndex = propsVectorTrie.get(c)
    return lineBreakFromVecIndex(vecIndex)

def sentenceBreakFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 2)
    return (props & UPROPS_SB_MASK) >> UPROPS_SB_SHIFT

def getSentenceBreak(c):
    vecIndex = propsVectorTrie.get(c)
    return sentenceBreakFromVecIndex(vecIndex)

def wordBreakFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 2)
    return (props & UPROPS_WB_MASK) >> UPROPS_WB_SHIFT

def getWordBreak(c):
    vecIndex = propsVectorTrie.get(c)
    return wordBreakFromVecIndex(vecIndex)

def graphemeClusterBreakFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 2)
    return (props & UPROPS_GCB_MASK) >> UPROPS_GCB_SHIFT

def getGraphemeClusterBreak(c):
    vecIndex = propsVectorTrie.get(c)
    return graphemeClusterBreakFromVecIndex(vecIndex)

def decompTypeFromVecIndex(vecIndex):
    props = unicodePropertiesFromVecIndex(vecIndex, 2)
    return props & UPROPS_DT_MASK

def getDecompType(c):
    vecIndex = propsVectorTrie.get(c)
    return decompTypeFromVecIndex(vecIndex)

def binaryPropFromVecIndex(vecIndex, propShift, column):
    props = unicodePropertiesFromVecIndex(vecIndex, column)
    return (props & (1 << propShift)) != 0

def getBinaryProp(c, propShift, column=1):
    if propShift >= UPROPS_BINARY_1_TOP:
        return None  # Or False?

    vecIndex = propsVectorTrie.get(c)
    return binaryPropFromVecIndex(vecIndex, propShift, column)

def isExtendedPictograph(c):
    return getBinaryProp(c, UPROPS_2_EXTENDED_PICTOGRAPHIC, 2)

def isEmojiComponent(c):
    return getBinaryProp(c, UPROPS_2_EMOJI_COMPONENT, 2)

def isEmoji(c):
    return getBinaryProp(c, UPROPS_2_EMOJI, 2)

def isEmojiPresentation(c):
    return getBinaryProp(c, UPROPS_2_EMOJI_PRESENTATION, 2)

def isEmojiModifier(c):
    return getBinaryProp(c, UPROPS_2_EMOJI_MODIFIER, 2)

def isEmojiModifierBase(c):
    return getBinaryProp(c, UPROPS_2_EMOJI_MODIFIER_BASE, 2)