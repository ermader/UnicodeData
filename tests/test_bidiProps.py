"""
Test for UnicodeData.BidiProps

Created on August 12, 2021

@author Eric Mader
"""

import pytest
from UnicodeData.UCDTypeDictionaries import bidiClassNames
from UnicodeData.UCDTypeDictionaries import joiningTypeNames as joiningTypes
from UnicodeData.UCDTypeDictionaries import joiningGroupNames as joiningGroups

from UnicodeData.BidiProps import getCharDirection, isBidiControl, isMirrored, getMirror, getPairedBracket, isJoinControl, getJoiningType, getJoiningGroup

charDirections = [
    ("+", "ES"),
    (",", "CS"),
    ("1", "EN"),
    ("a", "L"),
    (chr(0x05DC), "R"),   # HEBREW LETTER LAMED
    (chr(0x0644), "AL"),  # ARABIC LETTER LAM
    (chr(0x0667), "AN"),  # ARABIC-INDIC DIGIT SEVEN
    (chr(0x200C), "BN"),
    (chr(0x200D), "BN"),
    (chr(0x200E), "L"),
    (chr(0x200F), "R"),
    (chr(0x2028), "WS"),
    (chr(0x2029), "B"),
    (chr(0x202A), "LRE"),
    (chr(0x202B), "RLE"),
    (chr(0x202C), "PDF"),
    (chr(0x202D), "LRO"),
    (chr(0x202E), "RLO"),
    (chr(0x202F), "CS"),
    (chr(0x2066), "LRI"),
    (chr(0x2067), "RLI"),
    (chr(0x2068), "FSI"),
    (chr(0x2069), "PDI"),
]

@pytest.mark.parametrize("char, expectedDirection", charDirections)
def test_getCharDirection(char: str, expectedDirection: str):
    assert bidiClassNames[getCharDirection(ord(char))] == expectedDirection

def test_isBidiControl():
    assert not isBidiControl(0x200D)
    assert isBidiControl(0x200E)

def test_isMirrored():
    assert not isMirrored(ord("a"))
    assert isMirrored(ord("["))
    assert isMirrored(0x3010)  # LEFT BLACK LENTICULAR BRACKET
    assert not isMirrored(0x3042)  # HIRAGANA LETTER A

mirroredPairs = [
    ("(", ")"),
    ("{", "}"),
    ("«", "»"),
    ("【", "】")
]

@pytest.mark.parametrize("left, right", mirroredPairs)
def test_getMirror(left: str, right: str):
    assert getMirror(ord(left)) == ord(right)
    assert getMirror(ord(right)) == ord(left)

pairedBrackets = [
    ("(", ")"),
    ("[", "]"),
    ("{", "}"),
    ("【", "】")
]

@pytest.mark.parametrize("left, right", pairedBrackets)
def test_getPairedBracket(left: str, right: str):
    assert getPairedBracket(ord(left)) == ord(right)
    assert getPairedBracket(ord(right)) == ord(left)

def test_isJoiningControl():
    assert isJoinControl(0x200D)
    assert not isJoinControl(0x200E)

joiningTypeTests = [
    ("a", "U"),
    (chr(0x0627), "R"),
    (chr(0x0640), "C"),
    (chr(0x0644), "D"),
    (chr(0x064B), "T"),
    (chr(0x10ACD), "L"),
    (chr(0x10AD3), "D")
]

@pytest.mark.parametrize("char, expectedJoiningType", joiningTypeTests)
def test_getJoiningType(char: str, expectedJoiningType: str):
    assert joiningTypes[getJoiningType(ord(char))] == expectedJoiningType

joiningGroupTests = [
    (chr(0x0644), "Lam"),
    (chr(0x10AD3), "Manichaean Lamedh")
]

@pytest.mark.parametrize("char, expectedJoiningGroup", joiningGroupTests)
def test_getJoiningGroup(char: str, expectedJoiningGroup: str):
    assert joiningGroups[getJoiningGroup(ord(char))] == expectedJoiningGroup

