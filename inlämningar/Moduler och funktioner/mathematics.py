""" mathematics
This module is used for calculating
the sum, difference, product and
quotient of the given numbers
"""


def add(addend1, addend2):
    """Calculate the sum"""
    try:
        float_result = float(addend1) + float(addend2)

        if float_result == int(float_result):
            return int(float_result)
        else:
            return float_result
    except:
        return "Error: TypeError"


def sub(minuend, subtrahend):
    """Calculate the difference"""
    try:
        float_result = float(minuend) - float(subtrahend)

        if float_result == int(float_result):
            return int(float_result)
        else:
            return float_result
    except:
        return "Error: TypeError"


def mul(factor1, factor2):
    """Calculate the product"""
    try:
        float_result = float(factor1) * float(factor2)

        if float_result == int(float_result):
            return int(float_result)
        else:
            return float_result
    except:
        return "Error: TypeError"


def div(dividend, divisor):
    """Calculate the quotient"""
    try:
        float_result = float(dividend) / float(divisor)

        if float_result == int(float_result):
            return int(float_result)
        else:
            return float_result

    except ZeroDivisionError:
        return "Error: ZeroDivisionError"
    except:
        return "Error: TypeError"
