from enum import IntEnum




class GenericTimeEnum(IntEnum):
    am_0 = 0
    am_1 = 1
    am_2 = 2
    am_3 = 3
    am_4 = 4
    am_5 = 5
    am_6 = 6
    am_7 = 7
    am_8 = 8
    am_9 = 9
    am_10 = 10
    am_11 = 11
    pm_12 = 12
    pm_13 = 13
    pm_14 = 14
    pm_15 = 15
    pm_16 = 16
    pm_17 = 17
    pm_18 = 18
    pm_19 = 19
    pm_20 = 20
    pm_21 = 21
    pm_22 = 22
    pm_23 = 23

HOUR_DICT = {
    0: GenericTimeEnum.am_0,
    1: GenericTimeEnum.am_1,
    2: GenericTimeEnum.am_2,
    3: GenericTimeEnum.am_3,
    4: GenericTimeEnum.am_4,
    5: GenericTimeEnum.am_5,
    6: GenericTimeEnum.am_6,
    7: GenericTimeEnum.am_7,
    8: GenericTimeEnum.am_8,
    9: GenericTimeEnum.am_9,
    10: GenericTimeEnum.am_10,
    11: GenericTimeEnum.am_11,
    12: GenericTimeEnum.pm_12,
    13: GenericTimeEnum.pm_13,
    14: GenericTimeEnum.pm_14,
    15: GenericTimeEnum.pm_15,
    16: GenericTimeEnum.pm_16,
    17: GenericTimeEnum.pm_17,
    18: GenericTimeEnum.pm_18,
    19: GenericTimeEnum.pm_19,
    20: GenericTimeEnum.pm_20,
    21: GenericTimeEnum.pm_21,
    22: GenericTimeEnum.pm_22,
    23: GenericTimeEnum.pm_23,
}