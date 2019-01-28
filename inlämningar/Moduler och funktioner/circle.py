""" circle
This module is used for calculating a circles area
and circumference for a given radius
"""
from math import pi


def area(radius):
    """Calculate the area"""
    try:  # Try to convert whatever input to float.
        float_result = pi * abs(float(radius)) ** 2

        if float_result == int(float_result):  # If the float value equals the int value
            return int(float_result)  # the int value is returned.
        return float_result  # Otherwise the float is returned.
        # (same principle applies to all functions below)
    except:
        return "Error: TypeError"


def circ(radius):
    """Calculate the circumference"""
    try:
        float_result = 2 * pi * abs(float(radius))

        if float_result == int(float_result):
            return int(float_result)
        return float_result
    except:
        return "Error: TypeError"
