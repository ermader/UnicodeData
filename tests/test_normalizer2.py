"""
Test for UnicodeData.Normalizer2

Created on August 20, 2021

@author Eric Mader
"""

import typing

import pytest
from UnicodeData.Normalizer2 import nfcTrie, nfkcTrie, nfkc_cfTrie

CharList = typing.Optional[list[str]]

def stringToCharList(s: typing.Optional[str]) -> CharList:
    return [c for c in s] if s else None

charList = [0x0041, 0x0061, 0x00A0, 0x00A8, 0x00AD, 0x00BE, 0x00C0, 0x00E0, 0x0178, 0x1EA6, 0x3307, 0x6569, 0xCA8D,
            0xFA6C]

nfcTests = [
    (0x0041, None),
    (0x0061, None),
    (0x00A0, None),
    (0x00A8, None),
    (0x00AD, None),
    (0x00BE, None),
    (0x00C0, ['A', '\u0300']),
    (0x00E0, ['a', '\u0300']),
    (0x0178, ['Y', '\u0308']),
    (0x1EA6, ['A', '\u0302', '\u0300']),
    (0x3307, None),
    (0x6569, None),
    (0xCA8D, ['ᄍ', 'ᅧ', 'ᆰ']),
    (0xFA6C, ['\U000242EE']),
]

@pytest.mark.parametrize("char, expectedDecomp", nfcTests)
def test_nfc(char: int, expectedDecomp: CharList):
    assert stringToCharList(nfcTrie.getDecomposition(char)) == expectedDecomp

nfcRawTests = [
    (0x0041, None),
    (0x0061, None),
    (0x00A0, None),
    (0x00A8, None),
    (0x00AD, None),
    (0x00BE, None),
    (0x00C0, ['A', '\u0300']),
    (0x00E0, ['a', '\u0300']),
    (0x0178, ['Y', '\u0308']),
    (0x1EA6, ['\u00C2', '\u0300']),
    (0x3307, None),
    (0x6569, None),
    (0xCA8D, ['쪄', 'ᆰ']),
    (0xFA6C, ['\U000242EE']),
]

@pytest.mark.parametrize("char, expectedDecomp", nfcRawTests)
def test_nfcRaw(char: int, expectedDecomp: CharList):
    assert stringToCharList(nfcTrie.getRawDecomposition(char)) == expectedDecomp

nfkcTests = [
    (0x0041, None),
    (0x0061, None),
    (0x00A0, [' ']),
    (0x00A8, [' ', '\u0308']),
    (0x00AD, None),
    (0x00BE, ['3', '\u2044', '4']),
    (0x00C0, ['A', '\u0300']),
    (0x00E0, ['a', '\u0300']),
    (0x0178, ['Y', '\u0308']),
    (0x1EA6, ['A', '\u0302', '\u0300']),
    (0x3307, ['エ', 'ス', 'ク', 'ー', 'ト', '゙']),
    (0x6569, None),
    (0xCA8D, ['ᄍ', 'ᅧ', 'ᆰ']),
    (0xFA6C, ['\U000242EE']),
]

@pytest.mark.parametrize("char, expectedDecomp", nfkcTests)
def test_nfkc(char: int, expectedDecomp: CharList):
    assert stringToCharList(nfkcTrie.getDecomposition(char)) == expectedDecomp

nfkcRawTests = [
    (0x0041, None),
    (0x0061, None),
    (0x00A0, [' ']),
    (0x00A8, [' ', '\u0308']),
    (0x00AD, None),
    (0x00BE, ['3', '\u2044', '4']),
    (0x00C0, ['A', '\u0300']),
    (0x00E0, ['a', '\u0300']),
    (0x0178, ['Y', '\u0308']),
    (0x1EA6, ['\u00C2', '\u0300']),
    (0x3307, ['エ', 'ス', 'ク', 'ー', 'ド']),
    (0x6569, None),
    (0xCA8D, ['쪄', 'ᆰ']),
    (0xFA6C, ['\U000242EE']),
]

@pytest.mark.parametrize("char, expectedDecomp", nfkcRawTests)
def test_nfkcRaw(char: int, expectedDecomp: CharList):
    assert stringToCharList(nfkcTrie.getRawDecomposition(char)) == expectedDecomp

nfkc_cfTests = [
    (0x0041, ['a']),
    (0x0061, None),
    (0x00A0, [' ']),
    (0x00A8, [' ', '\u0308']),
    (0x00AD, None),
    (0x00BE, ['3', '\u2044', '4']),
    (0x00C0, ['a', '\u0300']),
    (0x00E0, ['a', '\u0300']),
    (0x0178, ['y', '\u0308']),
    (0x1EA6, ['a', '\u0302', '\u0300']),
    (0x3307, ['エ', 'ス', 'ク', 'ー', 'ト', '゙']),
    (0x6569, None),
    (0xCA8D, ['ᄍ', 'ᅧ', 'ᆰ']),
    (0xFA6C, ['\U000242EE']),
]

@pytest.mark.parametrize("char, expectedDecomp", nfkc_cfTests)
def test_nfkc_cf(char: int, expectedDecomp: CharList):
    assert stringToCharList(nfkc_cfTrie.getDecomposition(char)) == expectedDecomp

nfkc_cfRawTests = [
    (0x0041, ['a']),
    (0x0061, None),
    (0x00A0, [' ']),
    (0x00A8, [' ', '\u0308']),
    (0x00AD, None),
    (0x00BE, ['3', '\u2044', '4']),
    (0x00C0, ['\u00E0']),
    (0x00E0, ['a', '\u0300']),
    (0x0178, ['\u00FF']),
    (0x1EA6, ['\u1EA7']),
    (0x3307, ['エ', 'ス', 'ク', 'ー', 'ド']),
    (0x6569, None),
    (0xCA8D, ['쪄', 'ᆰ']),
    (0xFA6C, ['\U000242EE']),
]

@pytest.mark.parametrize("char, expectedDecomp", nfkc_cfRawTests)
def test_nfkc_cfRaw(char: int, expectedDecomp: CharList):
    assert stringToCharList(nfkc_cfTrie.getRawDecomposition(char)) == expectedDecomp

