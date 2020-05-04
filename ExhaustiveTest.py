from timeit import default_timer as timer

from UnicodeData import UnicodeCharacterData, CharacterData
import CharProps
import BidiProps
import Scripts
import Blocks
import GeneralCategories
import JoiningTypesAndGroups
import CharDirection

def doTest(cp, got, expected, name):
    if got != expected:
        print(f"    Code point {cp:04X} returned {name} {got}, expected {expected}")

def test():
    ucd = UnicodeCharacterData()

    print("  Starting exhaustive test:")

    start = timer()
    for (cp, characterData) in ucd.characterData.items():
        sc = Scripts.scriptCodes[CharProps.getScript(cp)]
        gc = GeneralCategories.generalCategories[CharProps.getGeneralCategory(cp)]
        cd = CharDirection.bidiClassNames[BidiProps.getCharDirection(cp)]
        jt = JoiningTypesAndGroups.joiningTypes[BidiProps.getJoiningType(cp)]
        jg = JoiningTypesAndGroups.joiningGroups[BidiProps.getJoiningGroup(cp)]
        bc = Blocks.blockNames[CharProps.getBlock(cp)]

        doTest(cp, sc, characterData.script, "script code")
        doTest(cp, gc, characterData.generalCategory, "general category")
        doTest(cp, cd, characterData.bidiProperties.bidiClass, "bidi class")
        doTest(cp, jt, characterData.joiningType, "joining type")
        doTest(cp, jg, characterData.joiningGroup, "joining group")
        doTest(cp, bc, characterData.block, "block code")

    end = timer()
    print(f"  Test took {end - start} seconds.")

if __name__ == "__main__":
    test()