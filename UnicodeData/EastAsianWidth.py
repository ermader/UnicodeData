"""\
Based on UEastAsianWidth from uchar.h in ICU

Created on May 4, 2020

@author Eric Mader
"""

U_EA_NEUTRAL = 0  # N
U_EA_AMBIGUOUS = 1  # A
U_EA_HALFWIDTH = 2  # H
U_EA_FULLWIDTH = 3  # F
U_EA_NARROW = 4  # Na
U_EA_WIDE = 5  # W

eastAsianWidthNames = {
    U_EA_NEUTRAL: "N",
    U_EA_AMBIGUOUS: "A",
    U_EA_HALFWIDTH: "H",
    U_EA_FULLWIDTH: "F",
    U_EA_NARROW: "Na",
    U_EA_WIDE: "W"
}
