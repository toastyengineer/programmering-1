"""
Hardlocked Calculator
"""

def addition(term1, term2):
    """Performs an addition of term1 and term2"""
    print("Addition Result:")
    print((float(term1)) + (float(term2)))


def subtraction(term1, term2):
    """Performs a subtraction of term1 and term2"""
    print("Subtraction Result:")
    print((float(term1)) - (float(term2)))


def multiplication(factor1, factor2):
    """Performs a multiplication of term1 and term2"""
    print("Multiplication Result:")
    print((float(factor1)) * (float(factor2)))


def division(numerator, denominator):
    """Performs a division of term1 and term2"""
    print("Division Result:")
    print((float(numerator)) / (float(denominator)))


def average(value1, value2):
    """Performs an average calculation of term1 and term2"""
    print("Average Result:")
    print(((float(value1)) + (float(value2))) / 2)


# Change any values below for different results


addition(2, 2)
subtraction(5, 4)
multiplication(5, 4)
division(128, 64)
average(5, 10)
