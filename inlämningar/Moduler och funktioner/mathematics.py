""" mathematics
This module is used for calculating
the sum, difference, product and
quotient of the given numbers
"""


def add(addend1, addend2):
    """Calculate the sum"""
    if type(addend1) is str or type(addend2) is str:
        return "Error: TypeError"
    else:
        return addend1 + addend2


def sub(minuend, subtrahend):
    """Calculate the difference"""
    try:
        return minuend - subtrahend
    except TypeError:
        return "Error: TypeError"


def mul(factor1, factor2):
    """Calculate the product"""
    if type(factor1) is str or type(factor2) is str:
        return "Error: TypeError"
    else:
        return factor1 * factor2


def div(dividend, divisor):
    """Calculate the quotient"""
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "Error: ZeroDivisionError"
    except TypeError:
        return "Error: TypeError"
