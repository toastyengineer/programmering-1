""" rectangle
This module is used for calculating
a rectangles area and circumference for
the given measurements
"""


def area(width, height):
    """Calculate the area"""
    try:
        float_result = abs(float(width) * float(height))

        if float_result == int(float_result):
            return int(float_result)
        else:
            return float_result
    except:
        return "Error: TypeError"


def circ(width, height):
    """Calculate the circumference"""
    try:
        float_result = 2 * (abs(float(width)) + abs(float(height)))

        if float_result == int(float_result):
            return int(float_result)
        else:
            return float_result
    except:
        return "Error: TypeError"
