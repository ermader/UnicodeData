"""/
ModuleBuilder. Build Python data from c files

Created on April 26, 2021

@author Eric Mader
"""

from datetime import datetime
import os
import re

class ModuleBuilder(object):
    def __init__(self, icuDirectory, cSourcePath, outDirectory, moduleName):
        sourcePath = os.path.join(icuDirectory, cSourcePath)
        os.makedirs(outDirectory, exist_ok=True)
        self.modulePath = os.path.join(outDirectory, moduleName)
        sourceFile = open(sourcePath)
        self.source = sourceFile.read()
        sourceFile.close()

        self.outputLines = ['"""/']

        todayString = datetime.now().astimezone().strftime("%B %_d, %Y at %I:%M:%S %p %Z")
        toolName = os.path.basename(__file__)
        fromName = os.path.basename(cSourcePath)

        self.outputLines.append(f"{moduleName}, based on {fromName} from ICU\n")
        self.outputLines.append(f"Generated by {toolName} on {todayString}")
        self.outputLines.append('"""\n')


    def getScalarDeclaration(self, name):
        # pattern = name + r"=([0-9]+);"
        pattern = name + r"=(.+);"
        return re.findall(pattern, self.source)[0]

    def getArrayDeclaration(self, arrayName):
        pattern = arrayName + r"\[.+?\]=\{(.+?)\};"
        return re.findall(pattern, self.source, re.DOTALL)[0]

    def getPropsDeclaration(self, name):
        pattern = name + r"=\{\n(.+?)\n\};"
        return re.findall(pattern, self.source, re.DOTALL)[0]

    def scalarToPython(self, name):
        declaration = self.getScalarDeclaration(name)
        self.outputLines.append(f"{name} = {declaration}\n")

    def arrayToPython(self, arrayName):
        array = self.getArrayDeclaration(arrayName)
        final = "\n" if "\n" in array else ""
        if array.endswith("\n"):
            array = array[:-1]
        if final:
            array = array.replace("\n", "\n    ")

        self.outputLines.append(f"{arrayName} = [{array}{final}]\n")

    def trieValues(self, trie, prefix):
        dict = {3: "index_length", 5: "index_2_null_offset", 6: "data_null_offset", 9: "high_start",
                10: "high_value_index"}
        values = []
        trieSplits = trie.split(",\n")

        for index, name in dict.items():
            self.outputLines.append(f"{prefix}_{name} = {trieSplits[index].strip()}")

        self.outputLines.append("")

    def trieValuesFromPropsDeclaration(self, propsName, prefix):
        propsDeclaration = self.getPropsDeclaration(propsName)
        trie = re.findall(r"\{\n(.+?)\}", propsDeclaration, re.DOTALL)[0]
        self.trieValues(trie, prefix)

    def trieValuesFromTrieDeclaration(self, trieName, prefix):
        trie = self.getPropsDeclaration(trieName)
        self.trieValues(trie, prefix)

    def writeFile(self):
        contents = "\n".join(self.outputLines)
        moduleFile = open(self.modulePath, "w")
        moduleFile.write(contents)
        moduleFile.close()

#
# ICU version number is in common/unicode/uvernum.h: e.g. #define U_ICU_VERSION_SHORT "69"
# ICU data file is in data/out in ICU build directory: e.g. data/out/icudt69l.dat. i.e. icudt + U_ICU_VERSION_SHORT + ("l" if littleEndian else "b") + .dat
# Unicode data version is in data/unidata/ppucd.txt: e.g. ucd;13.0.0
# Unicode data file is at https://www.unicode.org/Public/: e.g. https://www.unicode.org/Public/13.0.0
#

def build():
    icuSource = "/Users/emader/Downloads/icu69/icu4c/source"
    testDir = "test"

    bidiPropBuilder = ModuleBuilder(icuSource, "common/ubidi_props_data.h", testDir, "BidiPropsData.py")
    bidiPropBuilder.arrayToPython("ubidi_props_indexes")
    bidiPropBuilder.arrayToPython("ubidi_props_trieIndex")
    bidiPropBuilder.arrayToPython("ubidi_props_mirrors")
    bidiPropBuilder.arrayToPython("ubidi_props_jgArray")
    bidiPropBuilder.arrayToPython("ubidi_props_jgArray2")
    bidiPropBuilder.trieValuesFromPropsDeclaration("ubidi_props_singleton", "ubidi_props_trie")
    bidiPropBuilder.writeFile()

    charPropsBuilder = ModuleBuilder(icuSource, "common/uchar_props_data.h", testDir, "CharPropsData.py")
    charPropsBuilder.arrayToPython("propsTrie_index")
    charPropsBuilder.trieValuesFromTrieDeclaration("propsTrie", "propsTrie")
    charPropsBuilder.arrayToPython("propsVectorsTrie_index")
    charPropsBuilder.trieValuesFromTrieDeclaration("propsVectorsTrie", "propsVectorsTrie")
    charPropsBuilder.arrayToPython("propsVectors")
    charPropsBuilder.scalarToPython("propsVectorsColumns")
    charPropsBuilder.arrayToPython("scriptExtensions")
    charPropsBuilder.writeFile()

    casePropsBuilder = ModuleBuilder(icuSource, "common/ucase_props_data.h", testDir, "CasePropsData.py")
    casePropsBuilder.arrayToPython("ucase_props_indexes")
    casePropsBuilder.arrayToPython("ucase_props_trieIndex")
    casePropsBuilder.arrayToPython("ucase_props_exceptions")
    casePropsBuilder.arrayToPython("ucase_props_unfold")
    casePropsBuilder.trieValuesFromPropsDeclaration("ucase_props_singleton", "ucase_props_trie")
    casePropsBuilder.writeFile()

if __name__ == "__main__":
    build()
