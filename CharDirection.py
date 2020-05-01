"""\
Based on UCharDirection from uchar.h in ICU

Created on May 1, 2020

@author Eric Mader
"""

#  L @ stable ICU 2.0 * /
U_LEFT_TO_RIGHT = 0
#  R @ stable ICU 2.0 * /
U_RIGHT_TO_LEFT = 1
#  EN @ stable ICU 2.0 * /
U_EUROPEAN_NUMBER = 2
#  ES @ stable ICU 2.0 * /
U_EUROPEAN_NUMBER_SEPARATOR = 3
#  ET @ stable ICU 2.0 * /
U_EUROPEAN_NUMBER_TERMINATOR = 4
#  AN @ stable ICU 2.0 * /
U_ARABIC_NUMBER = 5
#  CS @ stable ICU 2.0 * /
U_COMMON_NUMBER_SEPARATOR = 6
#  B @ stable ICU 2.0 * /
U_BLOCK_SEPARATOR = 7
#  S @ stable ICU 2.0 * /
U_SEGMENT_SEPARATOR = 8
#  WS @ stable ICU 2.0 * /
U_WHITE_SPACE_NEUTRAL = 9
#  ON @ stable ICU 2.0 * /
U_OTHER_NEUTRAL = 10
#  LRE @ stable ICU 2.0 * /
U_LEFT_TO_RIGHT_EMBEDDING = 11
#  LRO @ stable ICU 2.0 * /
U_LEFT_TO_RIGHT_OVERRIDE = 12
#  AL @ stable ICU 2.0 * /
U_RIGHT_TO_LEFT_ARABIC = 13
#  RLE @ stable ICU 2.0 * /
U_RIGHT_TO_LEFT_EMBEDDING = 14
#  RLO @ stable ICU 2.0 * /
U_RIGHT_TO_LEFT_OVERRIDE = 15
#  PDF @ stable ICU 2.0 * /
U_POP_DIRECTIONAL_FORMAT = 16
#  NSM @ stable ICU 2.0 * /
U_DIR_NON_SPACING_MARK = 17
#  BN @ stable ICU 2.0 * /
U_BOUNDARY_NEUTRAL = 18
#  FSI @ stable ICU 52 * /
U_FIRST_STRONG_ISOLATE = 19
#  LRI @ stable ICU 52 * /
U_LEFT_TO_RIGHT_ISOLATE = 20
#  RLI @ stable ICU 52 * /
U_RIGHT_TO_LEFT_ISOLATE = 21
#  PDI @ stable ICU 52 * /
U_POP_DIRECTIONAL_ISOLATE = 22

bidiClassNames = {
    #  L @ stable ICU 2.0 * /
    U_LEFT_TO_RIGHT: 'L',
    #  R @ stable ICU 2.0 * /
    U_RIGHT_TO_LEFT: 'R',
    #  EN @ stable ICU 2.0 * /
    U_EUROPEAN_NUMBER: 'EN',
    #  ES @ stable ICU 2.0 * /
    U_EUROPEAN_NUMBER_SEPARATOR: 'ES',
    #  ET @ stable ICU 2.0 * /
    U_EUROPEAN_NUMBER_TERMINATOR: 'ET',
    #  AN @ stable ICU 2.0 * /
    U_ARABIC_NUMBER: 'AN',
    #  CS @ stable ICU 2.0 * /
    U_COMMON_NUMBER_SEPARATOR: 'CS',
    #  B @ stable ICU 2.0 * /
    U_BLOCK_SEPARATOR: 'B',
    #  S @ stable ICU 2.0 * /
    U_SEGMENT_SEPARATOR: 'S',
    #  WS @ stable ICU 2.0 * /
    U_WHITE_SPACE_NEUTRAL: 'WS',
    #  ON @ stable ICU 2.0 * /
    U_OTHER_NEUTRAL: 'ON',
    #  LRE @ stable ICU 2.0 * /
    U_LEFT_TO_RIGHT_EMBEDDING: 'LRE',
    #  LRO @ stable ICU 2.0 * /
    U_LEFT_TO_RIGHT_OVERRIDE: 'LRO',
    #  AL @ stable ICU 2.0 * /
    U_RIGHT_TO_LEFT_ARABIC: 'AL',
    #  RLE @ stable ICU 2.0 * /
    U_RIGHT_TO_LEFT_EMBEDDING: 'RLE',
    #  RLO @ stable ICU 2.0 * /
    U_RIGHT_TO_LEFT_OVERRIDE: 'RLO',
    #  PDF @ stable ICU 2.0 * /
    U_POP_DIRECTIONAL_FORMAT: 'PDF',
    #  NSM @ stable ICU 2.0 * /
    U_DIR_NON_SPACING_MARK: 'NSM',
    #  BN @ stable ICU 2.0 * /
    U_BOUNDARY_NEUTRAL: 'BN',
    #  FSI @ stable ICU 52 * /
    U_FIRST_STRONG_ISOLATE: 'FSI',
    #  LRI @ stable ICU 52 * /
    U_LEFT_TO_RIGHT_ISOLATE: 'LRI',
    #  RLI @ stable ICU 52 * /
    U_RIGHT_TO_LEFT_ISOLATE: 'RLI',
    #  PDI @ stable ICU 52 * /
    U_POP_DIRECTIONAL_ISOLATE: 'PDI'
}