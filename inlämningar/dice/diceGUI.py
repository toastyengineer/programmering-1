from random import randint
from tkinter import *
import tkinter.messagebox


def calc_func(rolls, wins, loss):
    while int(rolls) > 0:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        if dice1 + dice2 == 11 or dice1 + dice2 == 7 or dice1 == dice2:
            wins += 1
        else:
            loss += 1
        rolls -= 1

    percentage = (wins / (wins+loss)) * 100
    tkinter.messagebox.showinfo("Calculation", "Calculated percentage of a roll fulfilling requirements are:\n" + str(round(percentage, 1)) + "%")

def call_func(*args):
    wins = 0
    loss = 0
    rolls = int(entry_roll.get())
    calc_func(rolls, wins, loss)


def clearer(*args):
    entry_roll.delete(0, "end")


root = Tk()
root.title("Dice roller calculator")

info_label = Label(root, text="Please note that more rolls achieves a higher accuracy but at the cost of time.")
info_label.grid(row=0, columnspan=2, padx=10 , pady=(10, 0))

enter_num = Label(root, text="Enter number of rolls you would like to do:")
enter_num.grid(row=1, column=0, sticky=E, pady=5, padx=5)

entry_roll = Entry(root)
entry_roll.bind("<Return>", call_func)
entry_roll.grid(row=1, column=1, sticky=W, pady=5, padx=5)
rolls = entry_roll.get()

calc_btn = Button(root, text="Calculate", command=call_func).grid(row=2, column=1, sticky=E, pady=5, padx=5)
quit_btn = Button(root, text="Quit", command=root.quit).grid(row=2, column=0, sticky=W, pady=5, padx=5)
clear_btn = Button(root, text="Clear entry", command=clearer).grid(row=2, column=1, sticky=W)

root.mainloop()
