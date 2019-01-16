""" dice

This program will calculate the chance of getting
either 11, 7 as a sum of two rolled dices
OR that they are equal to each other.
"""

from random import randint

print()
ROLLS = int(input("Disclaimer: more rolls achieves a higher accuracy but at the cost of time.\n\
\nEnter the amount of rolls you want to do: "))
print()

WINS = 0
LOSS = 0

while ROLLS > 0:

    DICE_X = randint(1, 6)
    DICE_Y = randint(1, 6)

    if DICE_X+DICE_Y == 11 or DICE_X+DICE_Y == 7 or DICE_X == DICE_Y:
        WINS += 1
    else:
        LOSS += 1

    ROLLS -= 1
TOTAL = WINS + LOSS

PERCENTAGE = (WINS / TOTAL) * 100

print("Calculated percentage of a roll fulfilling requirements are:", round(PERCENTAGE, 1), "%")
