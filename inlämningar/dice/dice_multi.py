from random import randint
import multiprocessing
from multiprocessing import Pool
import time


def dice_calc(rolls, q):

    mutex.acquire()
    global wins
    global loss

    while rolls > 0:

        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        if dice1+dice2 == 11 or dice1+dice2 == 7 or dice1 == dice2:
            wins += 1

        else:
            loss += 1

        rolls -= 1
    ########
    # return wins and losses to queue
    q.put((wins, loss))
    ########
    mutex.release()

wins = 0
loss = 0
rolls = 1000000
mutex = multiprocessing.Lock()

if __name__ == "__main__":
    t = time.time()
    # #######
    # create a multiprocessing.Queue() instance that spans across Processes
    q = multiprocessing.Queue()
    # #######

    p1 = multiprocessing.Process(target=dice_calc, args=(rolls/4, q))
    p2 = multiprocessing.Process(target=dice_calc, args=(rolls/4, q))
    p3 = multiprocessing.Process(target=dice_calc, args=(rolls/4, q))
    p4 = multiprocessing.Process(target=dice_calc, args=(rolls/4, q))
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    ########
    #Get wins and losses from the queue
    for _ in range(4):
        item = q.get(timeout=5000)
        wins = wins + item[0]
        loss = loss + item[1]
    ########

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("You got", wins, " wins")
    print("You got", loss, " losses")
    print("You got", wins+loss, " in total")
    percentage = (wins / (wins + loss)) * 100
    print("Calculated percentage of a roll fulfilling requirements are:", round(percentage, 2), "%")

    print(round((time.time()-t), 3))