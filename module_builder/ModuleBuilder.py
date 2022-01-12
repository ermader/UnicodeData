"""/
ModuleBuilder. Build Python data from c files

Created on April 26, 2021

@author Eric Mader
"""

from datetime import datetime
import os
import re
from sys import argv, exit, stderr
import shutil
from pathlib import Path
from FontDocTools.ArgumentIterator import ArgumentIterator
from HeaderToPtyhon import HeaderFile
from UCDReader import UCDReader

class ModuleBuilderArgs:
    def __init__(self):
        self._icuSourceDir = ""
        self._outputDir = ""
        self._icuBuildDir = ""

    @property
    def icuSourceDir(self) -> str:
        return self._icuSourceDir

    @property
    def icuBuildDir(self) -> str:
        return self._icuBuildDir

    @property
    def outputDir(self) -> str:
        return self._outputDir

    @classmethod
    def forArguments(cls, argumentList: list[str]):
        args = ModuleBuilderArgs()
        args.processArguments(argumentList)
        return args

    def processArguments(self, argumentList: list[str]):
        arguments = ArgumentIterator(argumentList)
        argumentsSeen = {}

        for argument in arguments:
            if argument in argumentsSeen:
                raise ValueError("Duplicate option “" + argument + "”.")
            argumentsSeen[argument] = True

            self.processArgument(argument, arguments)

        self.completeInit()

    def processArgument(self, argument: str, arguments: ArgumentIterator):
        if argument == "--sourceDir":
            self._icuSourceDir = arguments.nextExtra("ICU Source Directory")
        elif argument == "--buildDir":
            self._icuBuildDir = arguments.nextExtra("ICU Build Directory")
        elif argument == "--outputDir":
            self._outputDir = arguments.nextExtra("Output Directory")
        else:
            raise ValueError(f"Unrecognized option “{argument}”.")

    def completeInit(self):
        """\
        Complete initialization of a shaping spec after some values have
        been set from the argument list.
        Check that required data has been provided and fill in defaults for others.
        Raise ValueError if required options are missing, or invalid option
        combinations are detected.
        """

        if not self._icuSourceDir:
            raise ValueError("Missing “--sourceDir” option.")

        if not self._icuBuildDir:
            raise ValueError("Missing “--buildDir” option.")

        if not self._outputDir:
            raise ValueError("Missing “--outputDir” option.")

#
# TODO:
#    include blank lines, comments before declarations
#    #defines with "{...}"?
#    handle definitions that use casts?
#

class ModuleBuilder(object):
    def __init__(self, icuDirectory: Path, cSourcePath: str, outDirectory: Path, moduleName: str):
        sourcePath = icuDirectory / cSourcePath
        os.makedirs(outDirectory, exist_ok=True)
        self.modulePath = outDirectory / moduleName
        sourceFile = open(sourcePath)
        self.source = sourceFile.read()
        sourceFile.close()

        self.outputLines = ['"""/']

        todayString = datetime.now().astimezone().strftime("%B %_d, %Y at %I:%M:%S %p %Z")
        toolName = Path(__file__).name
        fromName = sourcePath.name

        self.outputLines.append(f"{moduleName}, based on {fromName} from ICU\n")
        self.outputLines.append(f"Generated by {toolName} on {todayString}")
        self.outputLines.append('"""\n')


    def getScalarDeclaration(self, name: str) -> str:
        # pattern = name + r"=([0-9]+);"
        pattern = name + r"=(.+);"
        return re.findall(pattern, self.source)[0]

    def getArrayDeclaration(self, arrayName: str) -> str:
        pattern = arrayName + r"\[.+?\]=\{(.+?)\};"
        return re.findall(pattern, self.source, re.DOTALL)[0]

    def getPropsDeclaration(self, name: str) -> str:
        pattern = name + r"=\{\n(.+?)\n\};"
        return re.findall(pattern, self.source, re.DOTALL)[0]

    def scalarToPython(self, name: str):
        declaration = self.getScalarDeclaration(name)
        self.outputLines.append(f"{name} = {declaration}\n")

    def arrayToPython(self, arrayName: str):
        array = self.getArrayDeclaration(arrayName)
        final = "\n" if "\n" in array else ""
        if array.endswith("\n"):
            array = array[:-1]
        if final:
            array = array.replace("\n", "\n    ")

        self.outputLines.append(f"{arrayName} = [{array}{final}]\n")

    def trieValues(self, trie: str, prefix: str):
        dict = {3: "index_length", 5: "index_2_null_offset", 6: "data_null_offset", 9: "high_start",
                10: "high_value_index"}
        _values = []
        trieSplits = trie.split(",\n")

        for index, name in dict.items():
            self.outputLines.append(f"{prefix}_{name} = {trieSplits[index].strip()}")

        self.outputLines.append("")

    def trieValuesFromPropsDeclaration(self, propsName: str, prefix: str):
        propsDeclaration = self.getPropsDeclaration(propsName)
        trie = re.findall(r"\{\n(.+?)\}", propsDeclaration, re.DOTALL)[0]
        self.trieValues(trie, prefix)

    def trieValuesFromTrieDeclaration(self, trieName: str, prefix: str):
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
    argumentList = argv
    # args = None
    programName = Path(argumentList.pop(0)).name
    if len(argumentList) == 0:
        print(__doc__, file=stderr)
        exit(1)

    try:
        moduleBuilderArgs = ModuleBuilderArgs.forArguments(argumentList)
    except ValueError as error:
        print(programName + ": " + str(error), file=stderr)
        exit(1)

    icuSource = Path(moduleBuilderArgs.icuSourceDir)
    icuBuild = Path(moduleBuilderArgs.icuBuildDir)
    outDir = Path(moduleBuilderArgs.outputDir)

    bidiPropBuilder = ModuleBuilder(icuSource, "common/ubidi_props_data.h", outDir, "BidiPropsData.py")
    bidiPropBuilder.arrayToPython("ubidi_props_indexes")
    bidiPropBuilder.arrayToPython("ubidi_props_trieIndex")
    bidiPropBuilder.arrayToPython("ubidi_props_mirrors")
    bidiPropBuilder.arrayToPython("ubidi_props_jgArray")
    bidiPropBuilder.arrayToPython("ubidi_props_jgArray2")
    bidiPropBuilder.trieValuesFromPropsDeclaration("ubidi_props_singleton", "ubidi_props_trie")
    bidiPropBuilder.writeFile()

    charPropsBuilder = ModuleBuilder(icuSource, "common/uchar_props_data.h", outDir, "CharPropsData.py")
    charPropsBuilder.arrayToPython("propsTrie_index")
    charPropsBuilder.trieValuesFromTrieDeclaration("propsTrie", "propsTrie")
    charPropsBuilder.arrayToPython("propsVectorsTrie_index")
    charPropsBuilder.trieValuesFromTrieDeclaration("propsVectorsTrie", "propsVectorsTrie")
    charPropsBuilder.arrayToPython("propsVectors")
    charPropsBuilder.scalarToPython("propsVectorsColumns")
    charPropsBuilder.arrayToPython("scriptExtensions")
    charPropsBuilder.writeFile()

    casePropsBuilder = ModuleBuilder(icuSource, "common/ucase_props_data.h", outDir, "CasePropsData.py")
    casePropsBuilder.arrayToPython("ucase_props_indexes")
    casePropsBuilder.arrayToPython("ucase_props_trieIndex")
    casePropsBuilder.arrayToPython("ucase_props_exceptions")
    casePropsBuilder.arrayToPython("ucase_props_unfold")
    casePropsBuilder.trieValuesFromPropsDeclaration("ucase_props_singleton", "ucase_props_trie")
    casePropsBuilder.writeFile()

    uprops_h = HeaderFile(icuSource, "common/uprops.h", outDir)
    uprops_h.translate()
    uprops_h.writeFile()

    ucase_h = HeaderFile(icuSource, "common/ucase.h", outDir, ignore=["UCASECONTEXT_INITIALIZER"])
    ucase_h.translate()
    ucase_h.writeFile()

    uchar_h = HeaderFile(icuSource, "common/unicode/uchar.h", outDir, extraCode=["def U_MASK(x: int) -> int: return 1<<x\n"], ignore=["U_NO_NUMERIC_VALUE"])
    uchar_h.translate()
    uchar_h.writeFile()

    uscript_h = HeaderFile(icuSource, "common/unicode/uscript.h", outDir)
    uscript_h.translate()
    uscript_h.writeFile()

    uverFile = open(icuSource / "common/unicode/uvernum.h")
    uvData = uverFile.read()
    uverFile.close()
    icuVersion = re.findall(r'#define U_ICU_VERSION "([0-9.]+)"', uvData)[0]
    icuVersionShort = re.findall(r'#define U_ICU_VERSION_SHORT "([0-9]+)"', uvData)[0]
    print(f"ICU version = {icuVersion}, short version = {icuVersionShort}")

    # copy the icu data file from the icu build directory to the test directory
    shutil.copy(icuBuild / f"data/out/icudt{icuVersionShort}l.dat", outDir / "icudata.dat")
    shutil.copy(icuSource.parent / "LICENSE", outDir)

    # ppFile = open(icuSource / "data/unidata/ppucd.txt")
    # ppData = ppFile.read()
    # ppFile.close()
    #
    # ucdVersion = re.findall(r"ucd;([0-9.]+)", ppData)[0]

    ucdReader = UCDReader(icuSource, outDir)
    ucdReader.generateDictionaries()
    ucdReader.writeFile()

    ucdVersionFile = open(outDir / "UnicodeVersion.py", "w")
    ucdVersionFile.write(f'unicodeVersion = "{ucdReader.ucdVersion}"\n')
    ucdVersionFile.close()

if __name__ == "__main__":
    build()
