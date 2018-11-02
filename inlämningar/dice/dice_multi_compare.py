from random import randint
import time

t = time.time()

rolls = 10000000
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

print(wins+loss)
percentage = (wins / (wins+loss)) * 100

print("Calculated percentage of a roll fulfilling requirements are:", round(percentage, 2), "%")
print(round((time.time()-t), 3))
