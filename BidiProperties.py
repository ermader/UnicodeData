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

        self.bidiMirrored = self.getBooleanProperty("Bidi_M")

        bmg = self.getCharProperty("bmg")
        self.bidiMirroredGlyph = self.codePoint if bmg == "" else int(bmg, 16)

        self.bidiControl = self.getBooleanProperty("Bidi_C")

        self.bidiPairedBracketType = self.getCharProperty("bpt")
        bpb = self.getCharProperty("bpb")
        self.bidiPairedBracket = self.codePoint if bpb == "#" else int(bpb, 16)

        # Don't need these any more
        del self._char
        del self._group
