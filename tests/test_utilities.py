"""
Test for UnicodeData.Utilities

Created on August 20, 2021

@author Eric Mader
"""

import pytest
from UnicodeData.Utilities import isLead, isTrail, highBit, charFromSurrogates, surrogatesFromChar

def test_isLead():
    for ch in range(0xD800, 0xDC00):
        assert isLead(ch)

def test_isTrail():
    for ch in range(0xDC00, 0xE000):
        assert isTrail(ch)

highBitTests = [
    (0x00, None),
    (0x02, 1),
    (0x04, 2),
    (0x06, 2),
    (0x08, 3),
    (0x0A, 3),
    (0x0C, 3),
    (0x0E, 3),
    (0x10, 4),
    (0x3FF, 9),
    (0xFFFFFC00, 31),
    (0x200000000, 33),
    (0x123456789ABCDEF, 56),
]

@pytest.mark.parametrize("value, expectedHighBit", highBitTests)
def test_highBit(value, expectedHighBit):
    assert highBit(value) == expectedHighBit

surrogateTests = [
    (0xD800, 0xDC00, 0x10000),
    (0xD83D, 0xDE00, 0x1F600),
    (0xD850, 0xDEEE, 0x242EE),
    (0xDBFF, 0xDFFF, 0x10FFFF)
]

@pytest.mark.parametrize("lead, trail, char", surrogateTests)
def test_charFromSurrogates(lead, trail, char):
    assert charFromSurrogates(lead, trail) == char


@pytest.mark.parametrize("lead, trail, char", surrogateTests)
def test_surrogatesFromChar(lead, trail, char):
    assert surrogatesFromChar(char) == (lead, trail)
