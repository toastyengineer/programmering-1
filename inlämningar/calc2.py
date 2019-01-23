"""This program will calculate the sums for the functions below based on input numbers"""
#import time


def addition(term1, term2):
    """Add two numbers"""
    return (float(term1)) + (float(term2))


def subtraction(term1, term2):
    """Subtract two numbers"""
    return (float(term1)) - (float(term2))


def multiplication(factor1, factor2):
    """Multiply two numbers"""
    return (float(factor1)) * (float(factor2))


def division(numerator, denominator):
    """Divide two numbers"""
    if denominator == 0:
        return "Error"
    return (float(numerator)) / (float(denominator))


def average(value1, value2):
    """Average of two numbers"""
    return ((float(value1)) + (float(value2))) / 2


#print("Untitled Calculator V.2")

#time.sleep(1)

#print("You will now select two values to be processed by addition, \
#subtraction, division, multiplication and average.")

#time.sleep(3)

#NUM_1 = input("Please enter value 1: ")
#NUM_2 = input("Please enter value 2: ")

#print(addition(NUM_1, NUM_2))
#print(subtraction(NUM_1, NUM_2))
#print(multiplication(NUM_1, NUM_2))
#print(division(NUM_1, NUM_2))
#print(average(NUM_1, NUM_2))
