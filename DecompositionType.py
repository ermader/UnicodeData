"""\
Based on UDecomompositionType from uchar.h in ICU

Created on May 7, 2020

@author Eric Mader
"""

U_DT_NONE = 0              # [none]
U_DT_CANONICAL = 1         # [can]
U_DT_COMPAT = 2            # [com]
U_DT_CIRCLE = 3            # [enc]
U_DT_FINAL = 4             # [fin]
U_DT_FONT = 5              # [font]
U_DT_FRACTION = 6          # [fra]
U_DT_INITIAL = 7           # [init]
U_DT_ISOLATED = 8          # [iso]
U_DT_MEDIAL = 9            # [med]
U_DT_NARROW = 10            # [nar]
U_DT_NOBREAK = 11           # [nb]
U_DT_SMALL = 12             # [sml]
U_DT_SQUARE = 13            # [sqr]
U_DT_SUB = 14               # [sub]
U_DT_SUPER = 15             # [sup]
U_DT_VERTICAL = 16          # [vert]
U_DT_WIDE = 17              # [wide]

decompositionTypeNames = {
    U_DT_NONE: "none",
    U_DT_CANONICAL: "can",
    U_DT_COMPAT: "com",
    U_DT_CIRCLE: "enc",
    U_DT_FINAL: "fin",
    U_DT_FONT: "font",
    U_DT_FRACTION: "fra",
    U_DT_INITIAL: "init",
    U_DT_ISOLATED: "iso",
    U_DT_MEDIAL: "med",
    U_DT_NARROW: "nar",
    U_DT_NOBREAK: "nb",
    U_DT_SMALL: "sml",
    U_DT_SQUARE: "sqr",
    U_DT_SUB: "sub",
    U_DT_SUPER: "sup",
    U_DT_VERTICAL: "vert",
    U_DT_WIDE: "wide"
}
