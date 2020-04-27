'''\
Created on Apr 27, 2020

Indic properties.

@author: emader
'''

from UCDProperties import UCDProperties

class IndicProperties(UCDProperties):
    def __init__(self, char, group):
        UCDProperties.__init__(self, char, group)

        self.syllabicCategory = self.getCharProperty("InSC")
        self.matraCategory = self.getCharProperty("InMC")  # data file doesn't seem to have this property...
        self.positionalCategory = self.getCharProperty("InPC")

        # Don't need these any more
        self._char = None
        self._group = None