"""
Multi-core dice simulator
"""

from random import randint
import multiprocessing
import time

TIME = time.time()


def dice_calc(ROLLS, q):
    """Core of the application, keeps track of wins, losses and loops through the amount of rolls entered"""

    MUTEX.acquire()
    global WINS
    global LOSS

    while ROLLS > 0:

        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        if dice1+dice2 == 11 or dice1+dice2 == 7 or dice1 == dice2:
            WINS += 1

        else:
            LOSS += 1

        ROLLS -= 1
    ########
    # return wins and losses to queue
    q.put((WINS, LOSS))
    ########
    MUTEX.release()


WINS = 0
LOSS = 0

MUTEX = multiprocessing.Lock()

if __name__ == "__main__":

    multiprocessing.freeze_support()
    ROLLS = 2000000#int(input("Enter amount of rolls you would like to do: "))

    # #######
    # create a multiprocessing.Queue() instance that spans across Processes
    q = multiprocessing.Queue()
    # #######

    P1 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))
    P2 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))
    P3 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))
    P4 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))
    P5 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))
    P6 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))
    P7 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))
    P8 = multiprocessing.Process(target=dice_calc, args=(ROLLS / 8, q))

    P1.start()
    P2.start()
    P3.start()
    P4.start()
    P5.start()
    P6.start()
    P7.start()
    P8.start()

    # #######
    # Get wins and losses from the queue
    for _ in range(8):
        item = q.get(timeout=5000)
        WINS = WINS + item[0]
        LOSS = LOSS + item[1]
    # #######

    P1.join()
    P2.join()
    P3.join()
    P4.join()
    P5.join()
    P6.join()
    P7.join()
    P8.join()

    print(f"\nYou rolled a total of {WINS+LOSS} times, you got {WINS} wins and {LOSS} losses.")
    print(f"Calculated percentage of a roll fulfilling requirements are: {round((WINS / (WINS + LOSS)) * 100 , 4)}%\n")

    print(f"Finished in {round((time.time()-TIME), 3)} seconds.", end="\n\n")
