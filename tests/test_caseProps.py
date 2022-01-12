"""
Test for UnicodeData.CaseProps

Created on August 19, 2021

@author Eric Mader
"""

import pytest
from UnicodeData.CaseProps import toLower, toFullLower, toUpper, toFullUpper, toTitle, toFullTitle

toLowerTests = [
    ("A", "a"),
    ("a", "a"),
    (chr(0x0130), "i"),
    (chr(0x0131), chr(0x0131)),
]

@pytest.mark.parametrize("char, expectedLower", toLowerTests)
def test_toLower(char: str, expectedLower: str):
    assert chr(toLower(ord(char))) == expectedLower

toFullLowerTests = [
    ("A", "a"),
    ("a", "a"),
    (chr(0x0130), "i\u0307"),
    (chr(0x0131), chr(0x0131)),
]

@pytest.mark.parametrize("char, expectedLower", toFullLowerTests)
def test_toFullLower(char: str, expectedLower: str):
    assert toFullLower(ord(char)) == expectedLower

toUpperTests = [
    ("A", "A"),
    ("a", "A"),
    ("k", "K"),
    (chr(0x00DF), chr(0x00DF)),
    (chr(0x0130), chr(0x0130)),
    (chr(0x0131), "I"),
    (chr(0x0149), chr(0x0149)),
    ("Г", "Г"),
    ("г", "Г"),
    (chr(0x0587), chr(0x0587)),
    (chr(0x1E98), chr(0x1E98)),
]

@pytest.mark.parametrize("char, expecdtedUpper", toUpperTests)
def test_toUpper(char: str, expecdtedUpper: str):
    assert chr(toUpper(ord(char))) == expecdtedUpper

toFullUpperTests = [
    ("A", "A"),
    ("a", "A"),
    ("k", "K"),
    (chr(0x00DF), "SS"),
    (chr(0x0130), chr(0x0130)),
    (chr(0x0131), "I"),
    (chr(0x0149), "\u02BCN"),
    ("Г", "Г"),
    ("г", "Г"),
    (chr(0x0587), "\u0535\u0552"),
    (chr(0x1E98), "W\u030A"),
]

@pytest.mark.parametrize("char, expecdtedUpper", toFullUpperTests)
def test_toFullUpper(char: str, expecdtedUpper: str):
    assert toFullUpper(ord(char)) == expecdtedUpper

toTitleTests = [
    ("A", "A"),
    ("a", "A"),
    ("k", "K"),
    (chr(0x00DF), chr(0x00DF)),
    (chr(0x0130), chr(0x0130)),
    (chr(0x0131), "I"),
    (chr(0x0149), chr(0x0149)),
    ("Г", "Г"),
    ("г", "Г"),
    (chr(0x0587), chr(0x0587)),
    (chr(0x1E98), chr(0x1E98)),
]

@pytest.mark.parametrize("char, expectedTitle", toTitleTests)
def test_toTitle(char: str, expectedTitle: str):
    assert chr(toTitle(ord(char))) == expectedTitle

toFullTitleTests = [
    ("A", "A"),
    ("a", "A"),
    ("k", "K"),
    (chr(0x00DF), "Ss"),
    (chr(0x0130), chr(0x0130)),
    (chr(0x0131), "I"),
    (chr(0x0149), "\u02BCN"),
    ("Г", "Г"),
    ("г", "Г"),
    (chr(0x0587), "\u0535\u0582"),
    (chr(0x1E98), "W\u030A"),
]

@pytest.mark.parametrize("char, expectedTitle", toFullTitleTests)
def test_toFullTitle(char: str, expectedTitle: str):
    assert toFullTitle(ord(char)) == expectedTitle
