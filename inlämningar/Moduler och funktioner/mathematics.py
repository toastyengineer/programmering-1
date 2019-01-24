""" mathematics
This module is used for calculating
the sum, difference, product and
quotient of the given numbers
"""


def add(addend1, addend2):
    """Calculate the sum"""
    if isinstance(addend1, str) or isinstance(addend2, str):
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
    if isinstance(factor1, str) or isinstance(factor2, str):
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
