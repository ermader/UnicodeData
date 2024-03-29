'''\
Created on Apr 27, 2020

Indic properties.

@author: emader
'''

from xml.etree.ElementTree import Element
from .UCDProperties import UCDProperties

class IndicProperties(UCDProperties):
    def __init__(self, char: Element, group: Element):
        UCDProperties.__init__(self, char, group)

        self.syllabicCategory = self.getCharProperty("InSC")
        self.positionalCategory = self.getCharProperty("InPC")

        # Don't need these any more
        del self._char
        del self._group
