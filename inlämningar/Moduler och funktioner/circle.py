""" circle
This module is used for calculating
a circles area and circumference for
a given radius
"""
from math import pi


def area(radius):
    """Calculate the area"""
    try:
        return pi * abs(radius) ** 2
    except:
        return "Error: TypeError"


def circ(radius):
    """Calculate the circumference"""
    try:
        return 2 * pi * abs(radius)
    except:
        return "Error: TypeError"
