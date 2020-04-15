'''
Created on Apr 13, 2020

@author: emader
'''

import xml.etree.ElementTree as ElementTree
import pkg_resources

import CharacterData
import UnicodeSet

_characterData = {}
_scriptList = {}
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

            characterData = CharacterData.CharacterData(char, group)
            codePoint = characterData.getCodePoint()
            decomp = characterData.getDecomposition()
            script = characterData.getScript()

            _characterData[codePoint] = characterData

            if decomp is not None:
                _decompositions[codePoint] = decomp

            if script in _scriptList:
                _scriptList[script].add(codePoint)
            else:
                _scriptList[script] = UnicodeSet.UnicodeSet(codePoint)

def main():
    _populateCharacterData()

if __name__ == "__main__":
    main()
    for (script, unicodeSet) in _scriptList.items():
        ranges = unicodeSet.getRanges()
        s = "["

        for r in ranges:
            s += f"0x{r.start:04X}-0x{r.stop-1:04X}, "

        print(f"    '{script}': {s[:-2]}]")
    # print(_decompositions)
