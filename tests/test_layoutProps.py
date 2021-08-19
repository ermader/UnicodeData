"""
Test for UnicodeData.LayoutProps

Created on August 19, 2021

@author Eric Mader
"""

import pytest
import EnumeratorTests
from UnicodeData import LayoutTypes
from UnicodeData.LayoutProps import getInPC, getInSC, inpcTrie, inscTrie

def inPCEnumTest(start, limit):
    EnumeratorTests.testEnum( inpcTrie.enumerator, start=start, limit=limit, expectedFunction=getInPC, valueMapper=lambda v: LayoutTypes.inpcNames[v])

def inSCEnumTest(start, limit):
    EnumeratorTests.testEnum( inscTrie.enumerator, start=start, limit=limit, expectedFunction=getInSC, valueMapper=lambda v: LayoutTypes.inscNames[v])

inPCTests = [
    (chr(0x0901), "Top"),
    (chr(0x0903), "Right"),
    (chr(0x0915), "NA"),
    (chr(0x093A), "Top"),
    (chr(0x093B), "Right"),
    (chr(0x093C), "Bottom"),
    (chr(0x093E), "Right"),
    (chr(0x093F), "Left"),
    (chr(0x0940), "Right"),
    (chr(0x094D), "Bottom"),
    (chr(0x0B55), "Top"),
]

@pytest.mark.parametrize("char, expectedValue", inPCTests)
def test_getInPC(char, expectedValue):
    assert LayoutTypes.inpcNames[getInPC(ord(char))] == expectedValue

inSCTests = [
    ("0", "Number"),
    (chr(0x0900), "Bindu"),
    (chr(0x0901), "Bindu"),
    (chr(0x0902), "Bindu"),
    (chr(0x0903), "Visarga"),
    (chr(0x0904), "Vowel_Independent"),
    (chr(0x0915), "Consonant"),
    (chr(0x093A), "Vowel_Dependent"),
    (chr(0x093B), "Vowel_Dependent"),
    (chr(0x093C), "Nukta"),
    (chr(0x093D), "Avagraha"),
    (chr(0x094D), "Virama"),
    (chr(0x0950), "Other"),
    (chr(0x0964), "Other"),
    (chr(0x0966), "Number"),
]

@pytest.mark.parametrize("char, expectedValue", inSCTests)
def test_getInSC(char, expectedValue):
    assert LayoutTypes.inscNames[getInSC(ord(char))] == expectedValue

def test_inPCEnumeration():
    inPCEnumTest(0x0025, 0x0035)
    inPCEnumTest(0x0021, 0x007E)
    inPCEnumTest(0x0900, 0x0E00)
    inPCEnumTest(0xFF00, 0x1005F)
    inPCEnumTest(0x10005, 0x10015)

def test_inSCEnumeration():
    inSCEnumTest(0x0900, 0x0E00)
    inSCEnumTest(0x0E00, 0x0E80)


