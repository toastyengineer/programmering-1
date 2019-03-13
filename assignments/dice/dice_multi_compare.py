from random import randint
import time

t = time.time()

rolls = 2000000
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

percentage = (wins / (wins+loss)) * 100

print(f"\nYou rolled a total of {wins+loss} times, you got {wins} wins and {loss} losses.")
print(f"Calculated percentage of a roll fulfilling requirements are: {round(percentage, 4)}%\n")
print(f"Finished in {round((time.time()-t), 3)} seconds.", end="")
