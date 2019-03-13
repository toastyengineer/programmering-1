""" numberindex finder.py
Takes a number and a randomly generated list and
tries to find given number in the list.
"""
from random import randint


def find(array, number):
    """ Core """
    indexes = []
    for index in range(len(array)):
        if number == array[index]:
            indexes.append(index + 1)

    if indexes:  # If indexes list contains any value:
        return f"Number was found at following positions: {indexes}"
    return "Number was not found"


NUMBERLIST = []
for x in range(20):  # Generate a list with random number between 1-100
    NUMBERLIST.append(randint(1, 100))
print(NUMBERLIST)

REQUEST = int(input("Enter number you want to search for: "))

print(find(NUMBERLIST, REQUEST))
