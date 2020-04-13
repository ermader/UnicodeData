'''
Created on Apr 13, 2020

@author: emader
'''

import xml.etree.ElementTree as ElementTree
import pkg_resources

def getCharAttr(attribute, char, group):
    if attribute in char.attrib:
        return char.attrib[attribute]

    return group.get(attribute)

source = pkg_resources.resource_stream("ICUData", "Data/ucd.all.grouped.xml")
tree = ElementTree.parse(source)
root = tree.getroot()
nameSpaces = {"ucd": root.tag[1:-4]} # remove initial "{" and final "}ucd"

for group in root.findall("ucd:repertoire/ucd:group", nameSpaces):
    for char in group.findall("ucd:char", nameSpaces):
        cp = getCharAttr("cp", char, group)
        name = getCharAttr("na", char, group)
        script = getCharAttr("sc", char, group)
        block = getCharAttr("blk", char, group)

        if cp is None:
            continue

        name = name.replace("#", cp)

        print(f"{cp} {name} {script} {block}")

