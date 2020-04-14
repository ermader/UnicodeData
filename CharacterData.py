'''
Created on Apr 14, 2020

@author: emader
'''

class CharacterData:
    def getCharAttr(self, attribute, char, group):
        if attribute in char.attrib:
            return char.attrib[attribute]

        return group.get(attribute)

    def dmToString(self, dm):
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

    def __init__(self, char, group):
        cp = self.getCharAttr("cp", char, group)
        self.codePoint = int(cp, 16)

        self.name = self.getCharAttr("na", char, group)
        self.script = self.getCharAttr("sc", char, group)
        self.block = self.getCharAttr("blk", char, group)
        dm = self.getCharAttr("dm", char, group)

        if self.name is None or len(self.name) == 0:
            self.name = self.getCharAttr("na1", char, group)

        self.name = self.name.replace("#", cp)
        self.decomp = self.dmToString(dm)

    def getCodePoint(self):
        return self.codePoint

    def getScript(self):
        return self.script

    def getDecomposition(self):
        return self.decomp