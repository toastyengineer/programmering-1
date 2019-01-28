""" rectangle
This module is used for calculating
a rectangles area and circumference for
a rectangle with the given measurements
"""


def area(width, height):
    """Calculate the area"""
    try:  # Try to convert whatever input to float.
        float_result = abs(float(width) * float(height))

        if float_result == int(float_result):  # If the float value equals the int value
            return int(float_result)  # the int value is returned.
        return float_result  # Otherwise the float is returned.
        # (same principle applies to all functions below)
    except:
        return "Error: TypeError"


def circ(width, height):
    """Calculate the circumference"""
    try:
        float_result = 2 * (abs(float(width)) + abs(float(height)))

        if float_result == int(float_result):
            return int(float_result)
        return float_result
    except:
        return "Error: TypeError"
