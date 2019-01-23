"""
This module is used for calculating
a rectangles area and circumference for
the given measurements
"""


def area(width, height):
    """Calculate the area"""
    try:
        return abs(width * height)
    except TypeError:
        return "Error: TypeError"


def circ(width, height):
    """Calculate the circumference"""
    try:
        return 2 * (abs(width) + abs(height))
    except TypeError:
        return "Error: TypeError"
