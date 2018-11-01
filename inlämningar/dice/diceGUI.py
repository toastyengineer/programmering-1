from random import randint
from tkinter import *
import tkinter.messagebox
import webbrowser


def calc_func(entered_rolls):
    wins, loss = 0, 0
    while entered_rolls > 0:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        if dice1 + dice2 == 11 or dice1 + dice2 == 7 or dice1 == dice2:
            wins += 1
        else:
            loss += 1
        entered_rolls -= 1

    percentage = (wins / (wins+loss)) * 100
    tkinter.messagebox.showinfo("Calculation complete", "Calculated percentage of a roll fulfilling requirements are:\n" + str(round(percentage, 1)) + "%")


def call_calc(*args):
    if entry_roll.get().isdigit():
        entered_rolls = int(entry_roll.get())
        calc_func(entered_rolls)
    elif entry_roll.get() == "supersecret":
        tkinter.messagebox.showinfo("Wow", "You found an easter egg. Congratulations!")
        webbrowser.open('https://www.wikihow.com/Make-Pancakes')
    else:
        tkinter.messagebox.showwarning("Error", "Supplied roll amount is not valid input.")
        entry_roll.delete(0, "end")


def clearer():
    entry_roll.delete(0, "end")


def quitter():
    answer = tkinter.messagebox.askquestion("Quit", "Are you sure you want to quit the application?")
    if answer == "yes":
        root.quit()


root = Tk()
root.title("Dice Roller")
root.resizable(FALSE, FALSE)

info_label = Label(root, text="Please note that more rolls achieves a higher accuracy but at the cost of time.")
info_label.grid(row=0, columnspan=2, padx=10, pady=(5, 0))

enter_num = Label(root, text="Enter number of rolls you would like to do:")
enter_num.grid(row=1, column=0, sticky=E, pady=5, padx=5)

entry_roll = Entry(root)
entry_roll.bind("<Return>", call_calc)
entry_roll.grid(row=1, column=1, sticky=W, pady=5, padx=5)
rolls = entry_roll.get()

calc_btn = Button(root, text="Calculate", command=call_calc).grid(row=2, column=1, sticky=E, pady=5, padx=5)
quit_btn = Button(root, text="Quit", command=quitter).grid(row=2, column=0, sticky=W, pady=5, padx=5)
clear_btn = Button(root, text="Clear entry", command=clearer).grid(row=2, column=1, sticky=W)

root.mainloop()
