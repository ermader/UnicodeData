from timeit import default_timer as timer

from UnicodeData import UnicodeCharacterData, CharacterData
import CharProps
import BidiProps
import CaseProps
import LayoutProps
import Scripts
import Blocks
import EastAsianWidth
import GeneralCategories
import JoiningTypesAndGroups
import CharDirection
import Boundaries
import DecompositionType
import LayoutTypes
from CharNames import CharNames
from Normalizer2 import Normalizer2

def doTest(cp, got, expected, name):
    if got != expected:
        print(f"    Code point {cp:04X} returned {name} {got}, expected {expected}")

binaryTestList = [
    (CharProps.UPROPS_WHITE_SPACE, "whitespace"),
    (CharProps.UPROPS_DASH, "dash"),
    (CharProps.UPROPS_HYPHEN, "hyphen"),
    (CharProps.UPROPS_QUOTATION_MARK, "quotationMark"),
    (CharProps.UPROPS_TERMINAL_PUNCTUATION, "terminalPunctuation"),
    (CharProps.UPROPS_MATH, "math"),
    (CharProps.UPROPS_HEX_DIGIT, "hexDigit"),
    (CharProps.UPROPS_ASCII_HEX_DIGIT, "asciiHexDigit"),
    (CharProps.UPROPS_ALPHABETIC, "alphabetic"),
    (CharProps.UPROPS_IDEOGRAPHIC, "ideographic"),
    (CharProps.UPROPS_DIACRITIC, "diacritic"),
    (CharProps.UPROPS_EXTENDER, "extender"),
    (CharProps.UPROPS_NONCHARACTER_CODE_POINT, "nonCharacterCodePoint"),
    (CharProps.UPROPS_GRAPHEME_EXTEND, "graphemeExtended"),
    (CharProps.UPROPS_GRAPHEME_LINK, "graphemeLink"),
    (CharProps.UPROPS_IDS_BINARY_OPERATOR, "idsBinaryOperator"),
    (CharProps.UPROPS_IDS_TRINARY_OPERATOR, "idsTrinaryOperator"),
    (CharProps.UPROPS_RADICAL, "radical"),
    (CharProps.UPROPS_UNIFIED_IDEOGRAPH, "unifiedIdeographic"),
    (CharProps.UPROPS_DEFAULT_IGNORABLE_CODE_POINT, "defaultIgnorable"),
    (CharProps.UPROPS_DEPRECATED, "deprecated"),
    (CharProps.UPROPS_LOGICAL_ORDER_EXCEPTION, "logicalOrderException"),
    (CharProps.UPROPS_XID_START, "xIDStart"),
    (CharProps.UPROPS_XID_CONTINUE, "xIDContinue"),
    (CharProps.UPROPS_ID_START, "idStart"),
    (CharProps.UPROPS_ID_CONTINUE, "idContinue"),
    (CharProps.UPROPS_GRAPHEME_BASE, "graphemeBase"),
    (CharProps.UPROPS_S_TERM, "sentenceTerminalPunctuation"),
    (CharProps.UPROPS_VARIATION_SELECTOR, "variationSelector"),
    (CharProps.UPROPS_PATTERN_SYNTAX, "patternSyntax"),
    (CharProps.UPROPS_PATTERN_WHITE_SPACE, "patternWhitespace"),
    (CharProps.UPROPS_PREPENDED_CONCATENATION_MARK, "prependedConcatenationMark")
]

binaryTest2List = [
    (CharProps.UPROPS_2_EMOJI, "emoji"),
    (CharProps.UPROPS_2_EMOJI_PRESENTATION, "emojiPresentation"),
    (CharProps.UPROPS_2_EMOJI_MODIFIER, "emojiModifier"),
    (CharProps.UPROPS_2_EMOJI_MODIFIER_BASE, "emojiModifierBase"),
    (CharProps.UPROPS_2_EMOJI_COMPONENT, "emojiComponent"),
    (CharProps.UPROPS_2_EXTENDED_PICTOGRAPHIC, "extendedPictograph")
]

def doBinaryTests(cp, binaryProps):
    for (propMask, field) in binaryTestList:
        got = CharProps.getBinaryProp(cp, propMask)
        expected = getattr(binaryProps, field)
        doTest(cp, got, expected, field)

def doBinary2Tests(cp, charData):
    for (propsMask, field) in binaryTest2List:
        got = CharProps.getBinaryProp(cp, propsMask, 2)
        expected = getattr(charData, field)
        doTest(cp, got, expected, field)

def test():
    ucd = UnicodeCharacterData()
    normNFC = Normalizer2.createFromHardCodedData()
    normNFKC = Normalizer2.createFromFileData("nfkc")
    normNFKC_CF = Normalizer2.createFromFileData("nfkc_cf")

    print("  Starting exhaustive test:")

    start = timer()
    for (cp, characterData) in ucd.characterData.items():
        sc = Scripts.scriptCodes[CharProps.getScript(cp)]
        gc = GeneralCategories.generalCategories[CharProps.getGeneralCategory(cp)]
        cd = CharDirection.bidiClassNames[BidiProps.getCharDirection(cp)]
        jt = JoiningTypesAndGroups.joiningTypes[BidiProps.getJoiningType(cp)]
        jg = JoiningTypesAndGroups.joiningGroups[BidiProps.getJoiningGroup(cp)]
        bc = Blocks.blockNames[CharProps.getBlock(cp)]
        aw = EastAsianWidth.eastAsianWidthNames[CharProps.getEastAsianWidth(cp)]
        lb = Boundaries.lineBreakNames[CharProps.getLineBreak(cp)]
        sb = Boundaries.sentenceBreakNames[CharProps.getSentenceBreak(cp)]
        gcb = Boundaries.graphemeClusterBreakNames[CharProps.getGraphemeClusterBreak(cp)]
        bmg = BidiProps.getMirror(cp)
        bpb = BidiProps.getPairedBracket(cp)
        ijc = BidiProps.isJoinControl(cp)
        ibc = BidiProps.isBidiControl(cp)
        im = BidiProps.isMirrored(cp)
        dt = DecompositionType.decompositionTypeNames[CharProps.getDecompType(cp)]
        uc =CaseProps.toFullUpper(cp)
        lc = CaseProps.toFullLower(cp)
        tc = CaseProps.toFullTitle(cp)
        inpc = LayoutTypes.inpcNames[LayoutProps.getInPC(cp)]
        insc = LayoutTypes.inscNames[LayoutProps.getInSC(cp)]
        vo = LayoutTypes.voNames[LayoutProps.getVO(cp)]
        nfc = normNFC.getRawDecomposition(cp)
        nfkc = normNFKC.getRawDecomposition(cp)
        nfkc_cf = normNFKC_CF.getRawDecomposition(cp)
        name = CharNames.getCharName(cp)

        doTest(cp, sc, characterData.script, "script code")
        doTest(cp, gc, characterData.generalCategory, "general category")
        doTest(cp, cd, characterData.bidiProperties.bidiClass, "bidi class")
        doTest(cp, jt, characterData.joiningType, "joining type")
        doTest(cp, jg, characterData.joiningGroup, "joining group")
        doTest(cp, bc, characterData.block, "block code")
        doTest(cp, aw, characterData.eastAsianWidth, "East Asian width")
        doTest(cp, lb, characterData.lineBreak, "Line break")
        doTest(cp, sb, characterData.sentenceBreak, "Sentence break")
        doTest(cp, gcb, characterData.graphemeClusterBreak, "Grapheme cluster break")
        doTest(cp, bmg, characterData.bidiProperties.bidiMirroredGlyph, "bidi mirrored glyph")
        doTest(cp, bpb, characterData.bidiProperties.bidiPairedBracket, "bidi paired bracket")
        doTest(cp, ijc, characterData.isJoiningControl, "is joining control")
        doTest(cp, ibc, characterData.bidiProperties.bidiControl, "is bidi control")
        doTest(cp, im, characterData.bidiProperties.bidiMirrored, "is bidi mirrored")
        doTest(cp, dt, characterData.decompProperties.decompositionType, "decomposition type")
        doTest(cp, uc, characterData.caseProperties.upperCase, "upper case")
        doTest(cp, lc, characterData.caseProperties.lowerCase, "lower case")
        doTest(cp, tc, characterData.caseProperties.titleCase, "title case")
        doTest(cp, inpc, characterData.indicProperties.positionalCategory, "positional category")
        doTest(cp, insc, characterData.indicProperties.syllabicCategory, "syllabic category")
        doTest(cp, vo, characterData.verticalOrientation, "vertical orientation")

        if characterData.decompProperties.decompositionType == "can":
            doTest(cp, nfc, characterData.decompProperties.decomposition, "NFC decomposition")

        doTest(cp, nfkc, characterData.decompProperties.decomposition, "NFKC decomposition")

        # Really not sure about this:
        # - characters with decomp type "none" don't have a decomposition in the ICU data
        # - some charaters have an NFKC_CF of theselves, but the ICU data file has the normal decomposition
        if characterData.decompProperties.decompositionType != "none":
            if characterData.decompProperties.nfkcCaseFolded == chr(cp):
                expected = characterData.decompProperties.decomposition
            else:
                expected = characterData.decompProperties.nfkcCaseFolded

            doTest(cp, nfkc_cf, expected, "NFKC_CF decomposition")

        doTest(cp, name, characterData.name, "character name")

        doBinaryTests(cp, characterData.binaryProperties)
        doBinary2Tests(cp, characterData)

    end = timer()
    print(f"  Test took {end - start} seconds.")

if __name__ == "__main__":
    test()