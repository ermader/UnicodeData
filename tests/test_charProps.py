"""
Test for UnicodeData.CharProps

Created on August 12, 2021

@author Eric Mader
"""

import pytest

from UnicodeData.UCDTypeDictionaries import generalCategoryNames as generalCategories
from UnicodeData.UCDTypeDictionaries import scriptNames as scriptCodes
from UnicodeData.UCDTypeDictionaries import blockNames
from UnicodeData.uprops_h import *
from UnicodeData.UnicodeSet import UnicodeSet
from UnicodeData.CharProps import getAge, getBlock, getGeneralCategory, getScript, getNumericValue, digitValue, isAlphabetic, isUWhiteSpace, isHexDigit, \
    isEmoji, isEmojiModifier, isEmojiModifierBase, isEmojiComponent, isEmojiPresentation, isExtendedPictograph, \
    blockFromVecIndex, binaryPropFromVecIndex, generalCategoryFromProps, propsTrie, propsVectorTrie, scriptFromVecIndex

import EnumeratorTests

def unicodeSetAssertion(uset, assertion):
    for ch in uset:
        assert assertion(ch), f"'{chr(ch)}' fails {assertion.__name__}."

def gcEnumTest(start, limit):
    gcEnumerator = lambda start, limit: propsTrie.enumerator(start=start, limit=limit, valueFunction=generalCategoryFromProps)
    EnumeratorTests.testEnum(enumerator=gcEnumerator, start=start, limit=limit, \
                             expectedFunction=getGeneralCategory, valueMapper=lambda v: generalCategories[v])

def blockEnumTest(start, limit):
    EnumeratorTests.testEnum(lambda start, limit: propsVectorTrie.enumerator(start=start, limit=limit, valueFunction=blockFromVecIndex), \
                             start=start, limit=limit, expectedFunction=getBlock, valueMapper=lambda v: blockNames[v])

def emojiEnumTest(start, limit):
    EnumeratorTests.testEnum(lambda start, limit: propsVectorTrie.enumerator(start=start, limit=limit, valueFunction=binaryPropFromVecIndex, propShift=UPROPS_2_EMOJI, column=2), \
                             start=start, limit=limit, expectedFunction=isEmoji)

def scriptEnumTest(start, limit):
    EnumeratorTests.testEnum(lambda start, limit: propsVectorTrie.enumerator(start=start, limit=limit, valueFunction=scriptFromVecIndex), \
                             start=start, limit=limit, expectedFunction=getScript, valueMapper=lambda v: scriptCodes[v])

gcTests = [
    (chr(0x0012), "Cc"),
    ("3", "Nd"),
    ("(", "Ps"),
    (")", "Pe"),
    ("A", "Lu"),
    ("a", "Ll"),
    (chr(0x0644), "Lo"),  # ARABIC LETTER LAM
    (chr(0x0915), "Lo"),  # DEVANAGARI LETTER KA
    (chr(0x3010), "Ps"),  # LEFT BLACK LENTICULAR BRACKET
    (chr(0x3011), "Pe")   # RIGHT BLACK LENTICULAR BRACKET
]

@pytest.mark.parametrize("char, expectedGC", gcTests)
def test_getGeneralCatrgory(char, expectedGC):
    assert generalCategories[getGeneralCategory(ord(char))] == expectedGC

scriptTests = [
    ("A", 'Latn'),
    (chr(0x00C1), 'Latn'),
    (chr(0x0391), 'Grek'),
    (chr(0x0410), 'Cyrl'),
    (chr(0x0644), 'Arab'),
    (chr(0x0915), 'Deva'),
    (chr(0x0485), 'Zinh'),
    (chr(0x1E900), 'Adlm')
]

@pytest.mark.parametrize("char, expectedScript", scriptTests)
def test_getScript(char, expectedScript):
    assert scriptCodes[getScript(ord(char))] == expectedScript

numericValueTests = [
    ("0", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    (chr(0x00BC), 1/4),  # VULGAR FRACTION ONE QUARTER
    (chr(0x00BD), 1/2),  # VULGAR FRACTION ONE HALF
    (chr(0x00BE), 3/4),  # VULGAR FRACTION THREE QUARTERS
    (chr(0x0660), 0),  # ARABIC-INDIC DIGIT ZERO
    (chr(0x0661), 1),  # ARABIC-INDIC DIGIT ONE
    (chr(0x0662), 2),  # ARABIC-INDIC DIGIT TWO
    (chr(0x0663), 3),  # ARABIC-INDIC DIGIT THREE
    (chr(0x0664), 4),  # ARABIC-INDIC DIGIT FOUR
    (chr(0x0665), 5),  # ARABIC-INDIC DIGIT FIVE
    (chr(0x0666), 6),  # ARABIC-INDIC DIGIT SIX
    (chr(0x0667), 7),  # ARABIC-INDIC DIGIT SEVEN
    (chr(0x0668), 8),  # ARABIC-INDIC DIGIT EIGHT
    (chr(0x0669), 9),  # ARABIC-INDIC DIGIT NINE
    (chr(0x0966), 0),  # DEVANAGARI DIGIT ZERO
    (chr(0x0967), 1),
    (chr(0x0968), 2),
    (chr(0x0969), 3),
    (chr(0x096A), 4),
    (chr(0x096B), 5),
    (chr(0x096C), 6),
    (chr(0x096D), 7),
    (chr(0x096E), 8),
    (chr(0x096F), 9),

    (chr(0x09F4), 1/16),  # BENGALI CURRENCY NUMERATOR ONE
    (chr(0x09F5), 1/8),   # BENGALI CURRENCY NUMERATOR TWO
    (chr(0x09F6), 3/16),  # BENGALI CURRENCY NUMERATOR THREE
    (chr(0x09F7), 1/4),   # BENGALI CURRENCY NUMERATOR FOUR
    (chr(0x09F8), 3/4),   # BENGALI CURRENCY NUMERATOR ONE LESS THAN THE DENOMINATOR
    (chr(0x09F9), 16),    # BENGALI CURRENCY DENOMINATOR SIXTEEN

    (chr(0x0BE6), 0),     # TAMIL DIGIT 0
    (chr(0x0BE7), 1),
    (chr(0x0BE8), 2),
    (chr(0x0BE9), 3),
    (chr(0x0BEA), 4),
    (chr(0x0BEB), 5),
    (chr(0x0BEC), 6),
    (chr(0x0BED), 7),
    (chr(0x0BEE), 8),
    (chr(0x0BEF), 9),
    (chr(0x0BF0), 10),   # TAMIL NUMBER TEN
    (chr(0x0BF1), 100),  # TAMIL NUMBER ONE HUNDRED
    (chr(0x0BF2), 1000), # TAMIL NUMBER ONE THOUSAND

    (chr(0x4E00), 1),    # CJK IDEOGRAPHIC (1)
    (chr(0x4E8C), 2),    # CJK IDEOGRAPHIC (2)
    (chr(0x4E09), 3),    # CJK IDEOGRAPHIC (3)
    (chr(0x56DB), 4),    # CJK IDEOGRAPHIC (4)
    (chr(0x4E94), 5),    # CJK IDEOGRAPHIC (5)
    (chr(0x516D), 6),    # CJK IDEOGRAPHIC (6)
    (chr(0x4E03), 7),    # CJK IDEOGRAPHIC (7)
    (chr(0x516B), 8),    # CJK IDEOGRAPHIC (8)
    (chr(0x4E5D), 9),    # CJK IDEOGRAPHIC (9)
    (chr(0x5341), 10),   # CJK IDEOGRAPHIC (10)
    (chr(0x767E), 100),  # CJK IDEOGRAPHIC (100)
    (chr(0x5343), 1_000), # CJK IDEOGRAPHIC (1000)
    (chr(0x4E07), 10_000),# CJK IDEOGRAPHIC (10,000)
    (chr(0x5104), 100_000_000),  # CJK IDEOGRAPHIC (100,000,000)

    (chr(0x1ED01), 1),   # OTTOMAN SIYAQ NUMBER ONE
    (chr(0x1ED02), 2),
    (chr(0x1ED03), 3),
    (chr(0x1ED04), 4),
    (chr(0x1ED05), 5),
    (chr(0x1ED06), 6),
    (chr(0x1ED07), 7),
    (chr(0x1ED08), 8),
    (chr(0x1ED09), 9),
    (chr(0x1ED0A), 10),  # OTTOMAN SIYAQ NUMBER TEN
    (chr(0x1ED0B), 20),
    (chr(0x1ED0C), 30),
    (chr(0x1ED0D), 40),
    (chr(0x1ED0E), 50),
    (chr(0x1ED0F), 60),
    (chr(0x1ED10), 70),
    (chr(0x1ED11), 80),
    (chr(0x1ED12), 90),
    (chr(0x1ED13), 100), # OTTOMAN SIYAQ NUMBER ONE HUNDRED
    (chr(0x1ED14), 200),
    (chr(0x1ED15), 300),
    (chr(0x1ED16), 400),
    (chr(0x1ED17), 500),
    (chr(0x1ED18), 600),
    (chr(0x1ED19), 700),
    (chr(0x1ED1A), 800),
    (chr(0x1ED1B), 900),
    (chr(0x1ED1C), 1_000),  # OTTOMAN SIYAQ NUMBER ONE THOUSAND
    (chr(0x1ED1D), 2_000),
    (chr(0x1ED1E), 3_000),
    (chr(0x1ED1F), 4_000),
    (chr(0x1ED20), 5_000),
    (chr(0x1ED21), 6_000),
    (chr(0x1ED22), 7_000),
    (chr(0x1ED23), 8_000),
    (chr(0x1ED24), 9_000),
    (chr(0x1ED25), 10_000),  # OTTOMAN SIYAQ NUMBER TEN THOUSAND
    (chr(0x1ED26), 20_000),
    (chr(0x1ED27), 30_000),
    (chr(0x1ED28), 40_000),
    (chr(0x1ED29), 50_000),
    (chr(0x1ED2A), 60_000),
    (chr(0x1ED2B), 70_000),
    (chr(0x1ED2C), 80_000),
    (chr(0x1ED2D), 90_000),
]

# The fact that we have to skip any characters past 0x4E00 makes this test
# a bit suspicious. We should probably either drop it, or make another list...
@pytest.mark.parametrize("char, expectedNumericValue", numericValueTests)
def test_getNumericValue(char, expectedNumericValue):
    assert getNumericValue(ord(char)) == expectedNumericValue

@pytest.mark.parametrize("char, expectedValue", numericValueTests)
def test_digitValue(char, expectedValue):
    charCode = ord(char)
    actualValue = digitValue(charCode)
    if charCode < 0x4E00 and expectedValue in [x for x in range(10)]:
        assert expectedValue == actualValue
    else:
        assert actualValue == -1

alphaRanges = [
    UnicodeSet(range(ord("A"), ord("Z") + 1)),
    UnicodeSet(range(ord("a"), ord("z") + 1)),
    UnicodeSet(range(0x0391, 0x03FF)) - UnicodeSet(0x3A2) - UnicodeSet(0x03F6),  # Greek letters
    UnicodeSet(range(0x0400, 0x04FF)) - UnicodeSet(range(0x0482, 0x048A)),  # Cyrillic letters
    UnicodeSet(range(0x05D0, 0x05EA)),  # Hebrew Letters
    UnicodeSet(range(0x0620, 0x064B)) | UnicodeSet(range(0x066E, 0x0670)) | UnicodeSet(range(0x0671, 0x06D4)) | UnicodeSet(0x06D5) | UnicodeSet(range(0x6FA, 0x06FD)), # Arabic Letters
    UnicodeSet(range(0x0905, 0x093A)) | UnicodeSet(range(0x0958, 0x0962)) | UnicodeSet(range(0x0972, 0x0980)),  # Devanagari letters
    UnicodeSet(range(0x3041, 0x3097)),  # Hiragana letters
    UnicodeSet(range(0x30A1, 0x30FB)),  # Katakana letters
    UnicodeSet(range(0x3131, 0x318F)),  # Hangul letters
    UnicodeSet(range(0x10280, 0x1029D)),  # Lycian letters
    UnicodeSet(range(0x1E900, 0x1E943)),  # Adlam letters
]

@pytest.mark.parametrize("uset", alphaRanges)
def test_isAlphabetic(uset):
    unicodeSetAssertion(uset, isAlphabetic)

whitespaceChars = [
    UnicodeSet(0x0020),
    UnicodeSet(0x00A0),
    UnicodeSet(0x1680),
    UnicodeSet(range(0x2000, 0x200B)),
    UnicodeSet(0x202F),
    UnicodeSet(0x205F),
    UnicodeSet(0x3000),
]

@pytest.mark.parametrize("uset", whitespaceChars)
def test_isUWhiteSpace(uset):
    unicodeSetAssertion(uset, isUWhiteSpace)

hexDigits = [
    UnicodeSet(range(ord("0"), ord("9") + 1)),
    UnicodeSet(range(ord("A"), ord("F") + 1)),
    UnicodeSet(range(ord("a"), ord("f") + 1)),
    UnicodeSet(range(0xFF10, 0xFF1A)),  # Fullwidth digits
    UnicodeSet(range(0xFF21, 0xFF27)),  # fullwidth uppercase letters A-F
    UnicodeSet(range(0xFF41, 0xFF47)),  # fullwidth lowercase letters a-f
]

@pytest.mark.parametrize("uset", hexDigits)
def test_isHexDigit(uset):
    unicodeSetAssertion(uset, isHexDigit)

ageTests = [
    (chr(0x0218), [3, 0, 0, 0]),
    (chr(0x0220), [3, 2, 0, 0]),
    (chr(0x0234), [4, 0, 0, 0]),
    (chr(0x0237), [4, 1, 0, 0]),
    (chr(0x0242), [5, 0, 0, 0]),
]

@pytest.mark.parametrize("char, expectedAge", ageTests)
def test_getAge(char, expectedAge):
    assert getAge(ord(char)) == expectedAge

def test_isEmoji():
    assert isEmoji(0x1F600)
    assert isEmojiPresentation(0x231B)
    assert isEmojiModifier(0x1F3FB)
    assert isEmojiModifierBase(0x1F3C7)
    assert isEmojiComponent(0x1F9B0)
    assert isExtendedPictograph(0x1FA82)

def test_gcEumeration():
    gcEnumTest(start=0x25, limit=0x35)
    gcEnumTest(start=0x21, limit=0x7E)
    gcEnumTest(start=0x0020, limit=0x0080)

    gcEnumTest(start=0x0900, limit=0x0980)

    gcEnumTest(start=0xD800, limit=0xE000)

    gcEnumTest(start=0x1E900, limit=0x1E944)

def test_isEmojiEnum():
    emojiEnumTest(start=0x1F600, limit=0x1F680)

def test_enumBlocks():
    blockEnumTest(start=0x0300, limit=0x0400)
    blockEnumTest(start=0x0400, limit=0x0540)
    blockEnumTest(start=0x05D0, limit=0x0600)
    blockEnumTest(start=0x0600, limit=0x0700)
    blockEnumTest(start=0x0900, limit=0x0E00)
    blockEnumTest(start=0x1E900, limit=0x1E960)

def test_enumScripts():
    scriptEnumTest(start=0x0300, limit=0x0400)
    scriptEnumTest(start=0x0400, limit=0x0540)
    scriptEnumTest(start=0x05D0, limit=0x0600)
    scriptEnumTest(start=0x0600, limit=0x0700)
    scriptEnumTest(start=0x0900, limit=0x0E00)
    scriptEnumTest(start=0x0900, limit=0x0E00)
    scriptEnumTest(start=0x1E900, limit=0x1E960)

