'''\
Created on Apr 14, 2020

Bidirectional properties.

@author: emader
'''

from UCDProperties import UCDProperties

class BidiProperties(UCDProperties):
    """Bidirectional properties from the UCD file."""

    def __init__(self, char, group):
        UCDProperties.__init__(self, char, group)

        self.bidiClass = self.getCharProperty("bc")

        self.bidiMirrored = self.getCharProperty("Bidi_M") == "Y"  # works assuming that file is well-formed

        bmg = self.getCharProperty("bmg")
        self.bidiMirroredGlyph = bmg if bmg == "" else int(bmg, 16)

        self.bidiControl = self.getCharProperty("Bidi_C") == "Y"  # works assuming that file is well-formed

        self.bidiPairedBracketType = self.getCharProperty("bpt")
        bpb = self.getCharProperty("bpb")
        self.bidiPairedBracket = None if bpb == "#" else int(bpb, 16)  # maybe self.codePoint instead of None?
