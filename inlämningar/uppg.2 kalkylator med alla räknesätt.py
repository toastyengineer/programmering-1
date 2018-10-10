# ~ Anton Lundmark ~
import time

def addition(term1, term2):
    print("Addition Result:")
    print((float(term1)) + (float(term2)))

def subtraction(term1, term2):
    print("Subtraction Result:")
    print((float(term1)) - (float(term2)))

def multiplication(factor1, factor2):
    print("Multiplication Result:")
    print((float(factor1)) * (float(factor2)))

def division(numerator, denominator):
    print("Division Result:")
    print((float(numerator)) / (float(denominator)))

def average(value1, value2):
    print("Average Result:")
    print(((float(value1)) + (float(value2))) / 2)

print("Untitled Calculator v.1 2018")

time.sleep(1)

print("You will now select two values to be processed by addition, subtraction, division, multiplication and average.")

time.sleep(3)

number1 = input("Please enter value 1: ")
number2 = input("Please enter value 2: ")

addition(number1, number2)
subtraction(number1, number2)
multiplication(number1, number2)
division(number1, number2)
average(number1, number2)