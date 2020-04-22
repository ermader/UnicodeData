'''
Created on Apr 13, 2020

@author: emader
'''

import xml.etree.ElementTree as ElementTree
import pkg_resources

from CharacterData import CharacterData
from UnicodeSet import UnicodeSet

_characterData = {}
_generalCategories = {}
_bidiClasses = {}
_bidiPairedBracketTypes = {}
_scriptList = {}
_blockList = {}
_decompositions = {}

def getCharAttr(attribute, char, group):
    if attribute in char.attrib:
        return char.attrib[attribute]

    return group.get(attribute)

def dmToString(dm):
    # We don't care about characters that decompose to a single character -
    # they either decompose to themselves or are for compatibility.
    # We also don't care about decompositions that start w/ a space
    if " " not in dm or dm.startswith("0020 "):
        return None

    codePoints = dm.split(" ")
    str = ""
    for codePoint in codePoints:
        str += f"{int(codePoint, 16):c}"

    return str

def stringFromRanges(ranges):
    pieces = []

    for range in ranges:
        pieces.append(f"{range.start:04X}-{range.stop-1:04X}")

    s = ", ".join(pieces)
    return f"[{s}]"

def charsInSet(unicodeSet):
    chars = []
    len2 = len(unicodeSet.list) & ~1
    for i in range(0, len2, 2):
        start = unicodeSet.list[i]
        stop = unicodeSet.list[i+1]

        chars.extend([ch for ch in range(start, stop)])
    return chars

def _populateCharacterData():
    if len(_characterData) > 0:
        return

    source = pkg_resources.resource_stream("UnicodeData", "Data/ucd.all.grouped.xml")
    tree = ElementTree.parse(source)
    root = tree.getroot()
    nameSpaces = {"ucd": root.tag[1:-4]} # remove initial "{" and final "}ucd"

    for group in root.findall("ucd:repertoire/ucd:group", nameSpaces):
        for char in group.findall("ucd:char", nameSpaces):
            if "cp" not in char.attrib: # some entries are <char first-cp=xxxx last-cp=yyyy.../>
                continue

            characterData = CharacterData(char, group)
            codePoint = characterData.getCodePoint()
            generalCategory = characterData.getGeneralCategory()
            bidiClass = characterData.getBidiClass()
            bidiPairedBracketType = characterData.getBidiPairedBracketType()
            decomp = characterData.getDecomposition()
            script = characterData.getScript()
            block = characterData.getBlock()

            _characterData[codePoint] = characterData

            if generalCategory not in _generalCategories:
                _generalCategories[generalCategory] = UnicodeSet()
            _generalCategories[generalCategory].add(codePoint)

            if bidiClass not in _bidiClasses:
                _bidiClasses[bidiClass] = UnicodeSet()
            _bidiClasses[bidiClass].add(codePoint)

            if bidiPairedBracketType not in _bidiPairedBracketTypes:
                _bidiPairedBracketTypes[bidiPairedBracketType] = UnicodeSet()
            _bidiPairedBracketTypes[bidiPairedBracketType].add(codePoint)

            if decomp is not None:
                _decompositions[codePoint] = decomp

            if script not in _scriptList:
                _scriptList[script] = UnicodeSet()
            _scriptList[script].add(codePoint)

            if block not in _blockList:
                _blockList[block] = UnicodeSet()
            _blockList[block].add(codePoint)

def main():
    _populateCharacterData()

    for (script, unicodeSet) in _scriptList.items():
        ranges = unicodeSet.getRanges()
        print(f"    '{script}': {stringFromRanges(ranges)}")
    # print(_decompositions)

    devaSet = _scriptList['Deva']
    print(f"    devaSet.charAt(0x15) = {devaSet.charAt(0x15):04X}")
    print(f"    devaSet.charAt(106) = {devaSet.charAt(106):04X}")
    print(f"    devaSet.charAt(1000) = {devaSet.charAt(1000)}")
    print(f"    devaSet.indexOf(0x0970) = {devaSet.indexOf(0x0970)}")
    print(f"    devaSet.indexOf(0x0980) = {devaSet.indexOf(0x0980)}")

if __name__ == "__main__":
    main()
