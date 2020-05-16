"""\
Based on values from uchar.h in ICU

Created on May 14, 2020

@author Eric Mader
"""

# Indic positional category
U_INPC_NA = 0
U_INPC_BOTTOM = 1
U_INPC_BOTTOM_AND_LEFT = 2
U_INPC_BOTTOM_AND_RIGHT = 3
U_INPC_LEFT = 4
U_INPC_LEFT_AND_RIGHT = 5
U_INPC_OVERSTRUCK = 6
U_INPC_RIGHT = 7
U_INPC_TOP = 8
U_INPC_TOP_AND_BOTTOM = 9
U_INPC_TOP_AND_BOTTOM_AND_RIGHT = 10
U_INPC_TOP_AND_LEFT = 11
U_INPC_TOP_AND_LEFT_AND_RIGHT = 12
U_INPC_TOP_AND_RIGHT = 13
U_INPC_VISUAL_ORDER_LEFT = 14
U_INPC_TOP_AND_BOTTOM_AND_LEFT = 15

# Indic syllabic category
U_INSC_OTHER = 0
U_INSC_AVAGRAHA = 1
U_INSC_BINDU = 2
U_INSC_BRAHMI_JOINING_NUMBER = 3
U_INSC_CANTILLATION_MARK = 4
U_INSC_CONSONANT = 5
U_INSC_CONSONANT_DEAD = 6
U_INSC_CONSONANT_FINAL = 7
U_INSC_CONSONANT_HEAD_LETTER = 8
U_INSC_CONSONANT_INITIAL_POSTFIXED = 9
U_INSC_CONSONANT_KILLER = 10
U_INSC_CONSONANT_MEDIAL = 11
U_INSC_CONSONANT_PLACEHOLDER = 12
U_INSC_CONSONANT_PRECEDING_REPHA = 13
U_INSC_CONSONANT_PREFIXED = 14
U_INSC_CONSONANT_SUBJOINED = 15
U_INSC_CONSONANT_SUCCEEDING_REPHA = 16
U_INSC_CONSONANT_WITH_STACKER = 17
U_INSC_GEMINATION_MARK = 18
U_INSC_INVISIBLE_STACKER = 19
U_INSC_JOINER = 20
U_INSC_MODIFYING_LETTER = 21
U_INSC_NON_JOINER = 22
U_INSC_NUKTA = 23
U_INSC_NUMBER = 24
U_INSC_NUMBER_JOINER = 25
U_INSC_PURE_KILLER = 26
U_INSC_REGISTER_SHIFTER = 27
U_INSC_SYLLABLE_MODIFIER = 28
U_INSC_TONE_LETTER = 29
U_INSC_TONE_MARK = 30
U_INSC_VIRAMA = 31
U_INSC_VISARGA = 32
U_INSC_VOWEL = 33
U_INSC_VOWEL_DEPENDENT = 34
U_INSC_VOWEL_INDEPENDENT = 35

# vertical orientation
U_VO_ROTATED = 0
U_VO_TRANSFORMED_ROTATED = 1
U_VO_TRANSFORMED_UPRIGHT = 2
U_VO_UPRIGHT = 3

inpcNames = {
    U_INPC_NA: "NA",
    U_INPC_BOTTOM: "Bottom",
    U_INPC_BOTTOM_AND_LEFT: "Bottom_And_Left",
    U_INPC_BOTTOM_AND_RIGHT: "Bottom_And_Right",
    U_INPC_LEFT: "Left",
    U_INPC_LEFT_AND_RIGHT: "Left_And_Right",
    U_INPC_OVERSTRUCK: "Overstruck",
    U_INPC_RIGHT: "Right",
    U_INPC_TOP: "Top",
    U_INPC_TOP_AND_BOTTOM: "Top_And_Bottom",
    U_INPC_TOP_AND_BOTTOM_AND_RIGHT: "Top_And_Bottom_And_Right",
    U_INPC_TOP_AND_LEFT: "Top_And_Left",
    U_INPC_TOP_AND_LEFT_AND_RIGHT: "Top_And_Left_And_Right",
    U_INPC_TOP_AND_RIGHT: "Top_And_Right",
    U_INPC_VISUAL_ORDER_LEFT: "Visual_Order_Left",
    U_INPC_TOP_AND_BOTTOM_AND_LEFT: "Top_And_Bottom_And_Left"
}

inscNames = {
    U_INSC_OTHER: "Other",
    U_INSC_AVAGRAHA: "Avagraha",
    U_INSC_BINDU: "Bindu",
    U_INSC_BRAHMI_JOINING_NUMBER: "Brahmi_Joining_Number",
    U_INSC_CANTILLATION_MARK: "Cantillation_Mark",
    U_INSC_CONSONANT: "Consonant",
    U_INSC_CONSONANT_DEAD: "Consonant_Dead",
    U_INSC_CONSONANT_FINAL: "Consonant_Final",
    U_INSC_CONSONANT_HEAD_LETTER: "Consonant_Head_Letter",
    U_INSC_CONSONANT_INITIAL_POSTFIXED: "Consonant_Initial_Postfixed",
    U_INSC_CONSONANT_KILLER: "Consonant_Killer",
    U_INSC_CONSONANT_MEDIAL: "Consonant_Medial",
    U_INSC_CONSONANT_PLACEHOLDER: "Consonant_Placeholder",
    U_INSC_CONSONANT_PRECEDING_REPHA: "Consonant_Preceding_Repha",
    U_INSC_CONSONANT_PREFIXED: "Consonant_Prefixed",
    U_INSC_CONSONANT_SUBJOINED: "Consonant_Subjoined",
    U_INSC_CONSONANT_SUCCEEDING_REPHA: "Consonant_Succeeding_Repha",
    U_INSC_CONSONANT_WITH_STACKER: "Consonant_With_Stacker",
    U_INSC_GEMINATION_MARK: "Gemination_Mark",
    U_INSC_INVISIBLE_STACKER: "Invisible_Stacker",
    U_INSC_JOINER: "Joiner",
    U_INSC_MODIFYING_LETTER: "Modifying_Letter",
    U_INSC_NON_JOINER: "Non_Joiner",
    U_INSC_NUKTA: "Nukta",
    U_INSC_NUMBER: "Number",
    U_INSC_NUMBER_JOINER: "Number_Joiner",
    U_INSC_PURE_KILLER: "Pure_Killer",
    U_INSC_REGISTER_SHIFTER: "Register_Shifter",
    U_INSC_SYLLABLE_MODIFIER: "Syllable_Modifier",
    U_INSC_TONE_LETTER: "Tone_Letter",
    U_INSC_TONE_MARK: "Tone_Mark",
    U_INSC_VIRAMA: "Virama",
    U_INSC_VISARGA: "Visarga",
    U_INSC_VOWEL: "Vowel",
    U_INSC_VOWEL_DEPENDENT: "Vowel_Dependent",
    U_INSC_VOWEL_INDEPENDENT: "Vowel_Independent"
}

voNames = {
U_VO_ROTATED: "R",
U_VO_TRANSFORMED_ROTATED: "Tr",
U_VO_TRANSFORMED_UPRIGHT: "Tu",
U_VO_UPRIGHT: "U"
}
