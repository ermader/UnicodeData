'''
Created on Apr 13, 2020

@author: emader
'''

import xml.etree.ElementTree as ElementTree
from pathlib import Path
from timeit import default_timer as timer
#import shelve

from CharacterData import CharacterData
from UnicodeSet import UnicodeSet

_characterData = {}

def stringFromRanges(ranges):
    pieces = []

    for range in ranges:
        pieces.append(f"{range.start:04X}-{range.stop-1:04X}")

    s = ", ".join(pieces)
    return f"[{s}]"


def codePointsInSet(unicodeSet):
    chars = []
    len2 = len(unicodeSet.list) & ~1
    for i in range(0, len2, 2):
        start = unicodeSet.list[i]
        stop = unicodeSet.list[i+1]

        chars.extend([ch for ch in range(start, stop)])
    return chars



# def _populateCharacterData():
#     if len(_characterData) > 0:
#         return
#
#     source = Path("Data/ucd.all.grouped.xml")
#     tree = ElementTree.parse(source)
#     root = tree.getroot()
#     nameSpaces = {"ucd": root.tag[1:-4]} # remove initial "{" and final "}ucd"
#
#     for group in root.findall("ucd:repertoire/ucd:group", nameSpaces):
#         for char in group.findall("ucd:char", nameSpaces):
#             if "cp" not in char.attrib: # some entries are <char first-cp=xxxx last-cp=yyyy.../>
#                 continue
#
#             characterData = CharacterData(char, group)
#             codePoint = characterData.codePoint
#             _characterData[codePoint] = characterData
#
#
# _dbPath = str(Path("Data/unicode_data"))

class PropertyList(object):
    def __init__(self):
        self.dict = {}

    def __getitem__(self, key):
        if key not in self.dict:
            self.dict[key] = UnicodeSet()

        return self.dict[key]

    def addCodePointForKey(self, key, codePoint):
        self[key].add(codePoint)

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

class UnicodeCharacterData(object):

    characterData = {}

    @classmethod
    def _populateCharacterData(cls):
        if len(cls.characterData) > 0:
            return cls.characterData

        startTime = timer()
        source = Path("Data/ucd.all.grouped.xml")
        tree = ElementTree.parse(source)
        root = tree.getroot()
        ucdNameSpace = root.tag[1:-4]  # remove initial "{" and final "}ucd"
        nameSpaces = {"ucd": ucdNameSpace}

        for group in root.findall("ucd:repertoire/ucd:group", nameSpaces):
            for char in group.findall("ucd:char", nameSpaces):
                if "cp" not in char.attrib:  # some entries are <char first-cp=xxxx last-cp=yyyy.../>
                    continue

                characterData = CharacterData(char, group)
                codePoint = characterData.codePoint
                cls.characterData[codePoint] = characterData

        endTime = timer()
        print(f"  Reading {source.name} took {endTime - startTime} seconds.")

    def __init__(self):
        UnicodeCharacterData._populateCharacterData()


_scriptList = PropertyList()
_generalCategories = PropertyList()
_bidiClasses = PropertyList()
_bidiPairedBracketTypes = PropertyList()
_numericTypes = PropertyList()
_blockList = PropertyList()

_decompositions = {}


# when is it safe to close dataShelf?
def read():
    # start = timer()
    # dataShelf = shelve.open(_dbPath)
    # cd = dataShelf["ucd"]
    ucd = UnicodeCharacterData()

    for (cp, characterData) in ucd.characterData.items():
        codePoint = characterData.codePoint
        generalCategory = characterData.generalCategory
        bidiProps = characterData.bidiProperties
        bidiClass = bidiProps.bidiClass
        bidiPairedBracketType = bidiProps.bidiPairedBracketType
        decompProps = characterData.decompProperties
        decomposition = decompProps.decomposition
        numericType = characterData.numericType
        script = characterData.script
        block = characterData.block


        _generalCategories[generalCategory].add(codePoint)
        _bidiClasses[bidiClass].add(codePoint)
        _bidiPairedBracketTypes[bidiPairedBracketType].add(codePoint)

        if decomposition is not None:
            _decompositions[codePoint] = decomposition

        if numericType != "None":
            _numericTypes[numericType].add(codePoint)

        _scriptList[script].add(codePoint)
        _blockList[block].add(codePoint)

    # end = timer()
    # print(f"Reading unicode_data.db took {end - start} seconds.")
    return ucd


def main():
    cd = read()

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
