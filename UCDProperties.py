'''\
Created on Apr 23, 2020

A base class for fetching character properties from the UCD file.

@author: emader
'''

class UCDProperties(object):
    """A base class for fetching character properties from the UCD XML file."""

    def getCharProperty(self, property):
        """\
        Get the given character property. If the property
        isn't in the char element, get it from the enclosing group.

        :param property: the property to get
        :return: the property
        """
        if property in self._char.attrib:
            return self._char.attrib[property]

        return self._group.get(property)

    def __init__(self, char, group):
        """\
        Initialize with the char and group.

        :param char: the char element.
        :param group: the enclosing grouup element.
        """
        self._char = char
        self._group = group
