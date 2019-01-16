"""This program will calculate the sums for the functions below based on input numbers"""
import time


def addition(term1, term2):
    """Add two numbers"""
    print("Addition Result:")
    print((float(term1)) + (float(term2)))


def subtraction(term1, term2):
    """Subtract two numbers"""
    print("Subtraction Result:")
    print((float(term1)) - (float(term2)))


def multiplication(factor1, factor2):
    """Multiply two numbers"""
    print("Multiplication Result:")
    print((float(factor1)) * (float(factor2)))


def division(numerator, denominator):
    """Divide two numbers"""
    print("Division Result:")
    print((float(numerator)) / (float(denominator)))


def average(value1, value2):
    """Average of two numbers"""
    print("Average Result:")
    print(((float(value1)) + (float(value2))) / 2)


print("Untitled Calculator V.2")

time.sleep(1)

print("You will now select two values to be processed by addition, \
subtraction, division, multiplication and average.")

time.sleep(3)

NUM_1 = input("Please enter value 1: ")
NUM_2 = input("Please enter value 2: ")

addition(NUM_1, NUM_2)
subtraction(NUM_1, NUM_2)
multiplication(NUM_1, NUM_2)
division(NUM_1, NUM_2)
average(NUM_1, NUM_2)
