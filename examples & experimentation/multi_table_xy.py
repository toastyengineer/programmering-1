"""
Placeholder
"""

import time
NUM_1 = int(input("enter nm 1: "))
NUM_2 = int(input("enter nm 2: "))+1


for inputs in range(NUM_1, NUM_2):
    for factor in range(1, 11):
        if inputs*factor < 10:
            print(end=" ")
        if factor < 10:
            print(inputs*factor, end=", ")
        else:
            print(inputs*factor, end="\n")
time.sleep(180)

print()
