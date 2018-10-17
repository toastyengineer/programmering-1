from random import randint

print()
rolls = int(input("Disclaimer: more rolls achieves a higher accuracy but at the cost of time.\n\nEnter the amount of rolls you want to do: "))
print()

wins = 0
loss = 0

while rolls > 0:

    dice1 = randint(1, 6)
    dice2 = randint(1, 6)

    if dice1+dice2 == 11 or dice1+dice2 == 7 or dice1 == dice2:
        wins += 1
    else:
        loss += 1

    rolls -= 1
total = wins + loss

percentage = (wins / total) * 100

print("Calculated percentage of a roll fulfilling requirements are:", round(percentage, 1), "%")
