from random import randint
import multiprocessing
import time

t = time.time()


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

mutex = multiprocessing.Lock()

if __name__ == "__main__":

    multiprocessing.freeze_support()
    rolls = int(input("Enter amount of rolls you would like to do: "))

    # #######
    # create a multiprocessing.Queue() instance that spans across Processes
    q = multiprocessing.Queue()
    # #######

    p1 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))
    p2 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))
    p3 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))
    p4 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))
    p5 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))
    p6 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))
    p7 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))
    p8 = multiprocessing.Process(target=dice_calc, args=(rolls / 8, q))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()

    # #######
    # Get wins and losses from the queue
    for _ in range(8):
        item = q.get(timeout=5000)
        wins = wins + item[0]
        loss = loss + item[1]
    # #######

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()

    print(f"\nYou rolled a total of {wins+loss} times, you got {wins} wins and {loss} losses.")
    print(f"Calculated percentage of a roll fulfilling requirements are: {round((wins / (wins + loss)) * 100 , 2)}%\n")
    print(f"Finished in {round((time.time()-t), 3)} seconds.", end="\n\n")
    input("Press enter to continue...")
