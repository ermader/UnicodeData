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

        ccc = self.getCharAttr("ccc", char, group)
        self.combiningClass = int(ccc)

        self.name = self.getCharAttr("na", char, group)
        self.generalCategory = self.getCharAttr("gc", char, group)

        self.bidiClass = self.getCharAttr("bc", char, group)

        self.bidiMirrored = self.getCharAttr("Bidi_M", char, group) == "Y"  # works assuming that file is well-formed

        bmg = self.getCharAttr("bmg", char, group)
        self.bidiMirroredGlyph = bmg if bmg == "" else int(bmg, 16)

        self.bidiControl = self.getCharAttr("Bidi_C", char, group) == "Y"  # works assuming that file is well-formed

        self.bidiPairedBracketType = self.getCharAttr("bpt", char, group)
        bpb = self.getCharAttr("bpb", char, group)
        self.bidiPairedBracket = None if bpb == "#" else int(bpb, 16)  # maybe self.codePoint instead of None?

        self.script = self.getCharAttr("sc", char, group)
        self.block = self.getCharAttr("blk", char, group)
        dm = self.getCharAttr("dm", char, group)

        if self.name is None or len(self.name) == 0:
            self.name = self.getCharAttr("na1", char, group)

        self.name = self.name.replace("#", cp)
        self.decomp = self.dmToString(dm)

    def getCodePoint(self):
        return self.codePoint

    def getGeneralCategory(self):
        return self.generalCategory

    def getCombiningClass(self):
        return self.combiningClass

    def getBidiClass(self):
        return self.bidiClass

    def getBidiMirrored(self):
        return self.bidiMirrored

    def getBidiMirroredGlyph(self):
        return self.bidiMirroredGlyph

    def getBidiControl(self):
        return self.bidiControl

    def getBidiPairedBracketType(self):
        return self.bidiPairedBracketType

    def getBidiPairedBracket(self):
        return self.bidiPairedBracket

    def getScript(self):
        return self.script

    def getBlock(self):
        return self.block

    def getDecomposition(self):
        return self.decomp