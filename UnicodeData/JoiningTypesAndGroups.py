"""\
Based on types in uchar.h from ICU

Created on May 2, 2020

@author Eric Mader
"""

U_JT_NON_JOINING = 0  # [U]
U_JT_JOIN_CAUSING = 1  # [C]
U_JT_DUAL_JOINING = 2  # [D]
U_JT_LEFT_JOINING = 3  # [L]
U_JT_RIGHT_JOINING = 4  # [R]
U_JT_TRANSPARENT = 5  # [T]

joiningTypes = {
    U_JT_NON_JOINING: 'U',
    U_JT_JOIN_CAUSING: 'C',
    U_JT_DUAL_JOINING: 'D',
    U_JT_LEFT_JOINING: 'L',
    U_JT_RIGHT_JOINING: 'R',
    U_JT_TRANSPARENT: 'T'
}

U_JG_NO_JOINING_GROUP = 0
U_JG_AIN = 1
U_JG_ALAPH = 2
U_JG_ALEF = 3
U_JG_BEH = 4
U_JG_BETH = 5
U_JG_DAL = 6
U_JG_DALATH_RISH = 7
U_JG_E = 8
U_JG_FEH = 9
U_JG_FINAL_SEMKATH = 10
U_JG_GAF = 11
U_JG_GAMAL = 12
U_JG_HAH = 13
U_JG_TEH_MARBUTA_GOAL = 14
U_JG_HAMZA_ON_HEH_GOAL = U_JG_TEH_MARBUTA_GOAL
U_JG_HE = 15
U_JG_HEH = 16
U_JG_HEH_GOAL = 17
U_JG_HETH = 18
U_JG_KAF = 19
U_JG_KAPH = 20
U_JG_KNOTTED_HEH = 21
U_JG_LAM = 22
U_JG_LAMADH = 23
U_JG_MEEM = 24
U_JG_MIM = 25
U_JG_NOON = 26
U_JG_NUN = 27
U_JG_PE = 28
U_JG_QAF = 29
U_JG_QAPH = 30
U_JG_REH = 31
U_JG_REVERSED_PE = 32
U_JG_SAD = 33
U_JG_SADHE = 34
U_JG_SEEN = 35
U_JG_SEMKATH = 36
U_JG_SHIN = 37
U_JG_SWASH_KAF = 38
U_JG_SYRIAC_WAW = 39
U_JG_TAH = 40
U_JG_TAW = 41
U_JG_TEH_MARBUTA = 42
U_JG_TETH = 43
U_JG_WAW = 44
U_JG_YEH = 45
U_JG_YEH_BARREE = 46
U_JG_YEH_WITH_TAIL = 47
U_JG_YUDH = 48
U_JG_YUDH_HE = 49
U_JG_ZAIN = 50
U_JG_FE = 51
U_JG_KHAPH = 52
U_JG_ZHAIN = 53
U_JG_BURUSHASKI_YEH_BARREE = 54
U_JG_FARSI_YEH = 55
U_JG_NYA = 56
U_JG_ROHINGYA_YEH = 57
U_JG_MANICHAEAN_ALEPH = 58
U_JG_MANICHAEAN_AYIN = 59
U_JG_MANICHAEAN_BETH = 60
U_JG_MANICHAEAN_DALETH = 61
U_JG_MANICHAEAN_DHAMEDH = 62
U_JG_MANICHAEAN_FIVE = 63
U_JG_MANICHAEAN_GIMEL = 64
U_JG_MANICHAEAN_HETH = 65
U_JG_MANICHAEAN_HUNDRED = 66
U_JG_MANICHAEAN_KAPH = 67
U_JG_MANICHAEAN_LAMEDH = 68
U_JG_MANICHAEAN_MEM = 69
U_JG_MANICHAEAN_NUN = 70
U_JG_MANICHAEAN_ONE = 71
U_JG_MANICHAEAN_PE = 72
U_JG_MANICHAEAN_QOPH = 73
U_JG_MANICHAEAN_RESH = 74
U_JG_MANICHAEAN_SADHE = 75
U_JG_MANICHAEAN_SAMEKH = 76
U_JG_MANICHAEAN_TAW = 77
U_JG_MANICHAEAN_TEN = 78
U_JG_MANICHAEAN_TETH = 79
U_JG_MANICHAEAN_THAMEDH = 80
U_JG_MANICHAEAN_TWENTY = 81
U_JG_MANICHAEAN_WAW = 82
U_JG_MANICHAEAN_YODH = 83
U_JG_MANICHAEAN_ZAYIN = 84
U_JG_STRAIGHT_WAW = 85
U_JG_AFRICAN_FEH = 86
U_JG_AFRICAN_NOON = 87
U_JG_AFRICAN_QAF = 88
U_JG_MALAYALAM_BHA = 89
U_JG_MALAYALAM_JA = 90
U_JG_MALAYALAM_LLA = 91
U_JG_MALAYALAM_LLLA = 92
U_JG_MALAYALAM_NGA = 93
U_JG_MALAYALAM_NNA = 94
U_JG_MALAYALAM_NNNA = 95
U_JG_MALAYALAM_NYA = 96
U_JG_MALAYALAM_RA = 97
U_JG_MALAYALAM_SSA = 98
U_JG_MALAYALAM_TTA = 99
U_JG_HANIFI_ROHINGYA_KINNA_YA = 100
U_JG_HANIFI_ROHINGYA_PA = 101

joiningGroups = {
    U_JG_NO_JOINING_GROUP: "No Joining Group",
    U_JG_AIN: "Ain",
    U_JG_ALAPH: "Alaph",
    U_JG_ALEF: "Alef",
    U_JG_BEH: "Beh",
    U_JG_BETH: "Beth",
    U_JG_DAL: "Dal",
    U_JG_DALATH_RISH: "Dalath Rish",
    U_JG_E: "E",
    U_JG_FEH: "Feh",
    U_JG_FINAL_SEMKATH: "Final Semkath",
    U_JG_GAF: "Gaf",
    U_JG_GAMAL: "Gamal",
    U_JG_HAH: "Hah",
    U_JG_TEH_MARBUTA_GOAL: "Teh Marbuta Goal",
    U_JG_HE: "He",
    U_JG_HEH: "Heh",
    U_JG_HEH_GOAL: "Heh Goal",
    U_JG_HETH: "Heth",
    U_JG_KAF: "Kaf",
    U_JG_KAPH: "Kaph",
    U_JG_KNOTTED_HEH: "Knotted Heh",
    U_JG_LAM: "Lam",
    U_JG_LAMADH: "Lamadh",
    U_JG_MEEM: "Meem",
    U_JG_MIM: "Mim",
    U_JG_NOON: "Noon",
    U_JG_NUN: "Nun",
    U_JG_PE: "Pe",
    U_JG_QAF: "Qaf",
    U_JG_QAPH: "Qaph",
    U_JG_REH: "Reh",
    U_JG_REVERSED_PE: "Reversed Pe",
    U_JG_SAD: "Sad",
    U_JG_SADHE: "Sadhe",
    U_JG_SEEN: "Seen",
    U_JG_SEMKATH: "Semkath",
    U_JG_SHIN: "Shin",
    U_JG_SWASH_KAF: "Swash Kaf",
    U_JG_SYRIAC_WAW: "Syriac Waw",
    U_JG_TAH: "Tah",
    U_JG_TAW: "Taw",
    U_JG_TEH_MARBUTA: "Teh Marbuta",
    U_JG_TETH: "Teth",
    U_JG_WAW: "Waw",
    U_JG_YEH: "Yeh",
    U_JG_YEH_BARREE: "Yeh Barree",
    U_JG_YEH_WITH_TAIL: "Yeh With Tail",
    U_JG_YUDH: "Yudh",
    U_JG_YUDH_HE: "Yudh He",
    U_JG_ZAIN: "Zain",
    U_JG_FE: "Fe",
    U_JG_KHAPH: "Khaph",
    U_JG_ZHAIN: "Zhain",
    U_JG_BURUSHASKI_YEH_BARREE: "Burushaski Yeh Barree",
    U_JG_FARSI_YEH: "Farsi Yeh",
    U_JG_NYA: "Nya",
    U_JG_ROHINGYA_YEH: "Rohingya Yeh",
    U_JG_MANICHAEAN_ALEPH: "Manichaean Aleph",
    U_JG_MANICHAEAN_AYIN: "Manichaean Ayin",
    U_JG_MANICHAEAN_BETH: "Manichaean Beth",
    U_JG_MANICHAEAN_DALETH: "Manichaean Daleth",
    U_JG_MANICHAEAN_DHAMEDH: "Manichaean Dhamedh",
    U_JG_MANICHAEAN_FIVE: "Manichaean Five",
    U_JG_MANICHAEAN_GIMEL: "Manichaean Gimel",
    U_JG_MANICHAEAN_HETH: "Manichaean Heth",
    U_JG_MANICHAEAN_HUNDRED: "Manichaean Hundred",
    U_JG_MANICHAEAN_KAPH: "Manichaean Kaph",
    U_JG_MANICHAEAN_LAMEDH: "Manichaean Lamedh",
    U_JG_MANICHAEAN_MEM: "Manichaean Mem",
    U_JG_MANICHAEAN_NUN: "Manichaean Nun",
    U_JG_MANICHAEAN_ONE: "Manichaean One",
    U_JG_MANICHAEAN_PE: "Manichaean Pe",
    U_JG_MANICHAEAN_QOPH: "Manichaean Qoph",
    U_JG_MANICHAEAN_RESH: "Manichaean Resh",
    U_JG_MANICHAEAN_SADHE: "Manichaean Sadhe",
    U_JG_MANICHAEAN_SAMEKH: "Manichaean Samekh",
    U_JG_MANICHAEAN_TAW: "Manichaean Taw",
    U_JG_MANICHAEAN_TEN: "Manichaean Ten",
    U_JG_MANICHAEAN_TETH: "Manichaean Teth",
    U_JG_MANICHAEAN_THAMEDH: "Manichaean Thamedh",
    U_JG_MANICHAEAN_TWENTY: "Manichaean Twenty",
    U_JG_MANICHAEAN_WAW: "Manichaean Waw",
    U_JG_MANICHAEAN_YODH: "Manichaean Yodh",
    U_JG_MANICHAEAN_ZAYIN: "Manichaean Zayin",
    U_JG_STRAIGHT_WAW: "Straight Waw",
    U_JG_AFRICAN_FEH: "African Feh",
    U_JG_AFRICAN_NOON: "African Noon",
    U_JG_AFRICAN_QAF: "African Qaf",
    U_JG_MALAYALAM_BHA: "Malayalam Bha",
    U_JG_MALAYALAM_JA: "Malayalam Ja",
    U_JG_MALAYALAM_LLA: "Malayalam Lla",
    U_JG_MALAYALAM_LLLA: "Malayalam Llla",
    U_JG_MALAYALAM_NGA: "Malayalam Nga",
    U_JG_MALAYALAM_NNA: "Malayalam Nna",
    U_JG_MALAYALAM_NNNA: "Malayalam Nnna",
    U_JG_MALAYALAM_NYA: "Malayalam Nya",
    U_JG_MALAYALAM_RA: "Malayalam Ra",
    U_JG_MALAYALAM_SSA: "Malayalam Ssa",
    U_JG_MALAYALAM_TTA: "Malayalam Tta",
    U_JG_HANIFI_ROHINGYA_KINNA_YA: "Hanifi Rohingya Kinna Ya",
    U_JG_HANIFI_ROHINGYA_PA: "Hanifi Rohingya Pa"
}

def fixup():
    for (code, name) in joiningGroups.items():
        symbol = f"U_{name}"
        newName = name[3:].title().replace("_", " ")
        print(f'    {symbol}: "{newName}",')

if __name__ == "__main__":
    fixup()
