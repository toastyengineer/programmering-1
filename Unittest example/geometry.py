"""Yep yep yep"""

import math


def rectangle_area(langd, bredd):
    """Calculate Rectangle Area"""
    return abs(langd) * abs(bredd)


def rectangle_omkrets(langd, bredd):
    """Calculate Rectangle Circumference"""
    return 2 * (abs(langd) + abs(bredd))


def rectangle_ratio(langd, bredd):
    """Calculate Rectangle Ratio"""
    if bredd != 0:
        return abs(langd) / abs(bredd)
    else:
        return 0


def rectangle_hypotenuse(langd, bredd):
    """Calculate Rectangle Hypotenuse"""
    return math.sqrt((langd ** 2) + (bredd ** 2))
