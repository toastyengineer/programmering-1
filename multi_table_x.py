"""
Placeholder
"""


def multiplicator(num):
    """Core of the program, multiplies and prints all the numbers"""
    for numbers in range(1, 11):
        if numbers < 10:
            print(int(num) * numbers, end=", ")
        else:
            print(int(num) * numbers, end=" ")


USER_INPUT = input("Enter number to preview its multiplication table: ")
multiplicator(USER_INPUT)
