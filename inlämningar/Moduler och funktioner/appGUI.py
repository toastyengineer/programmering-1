import mathematics, rectangle, circle
from tkinter import *
import tkinter.messagebox


def call_calc():
    calculate(num1.get(), num2.get())


def calculate(number1, number2):
    print(mathematics.add(number1, number2))


def quitter():
    answer = tkinter.messagebox.askquestion("Quit", "Are you sure you want to quit?")
    if answer == "yes":
        exit()

root = Tk()
root.title("Application")
root.resizable(FALSE, FALSE)

label_num = Label(root, text="Enter the first number/measurement:")
label_num.grid(row=0, column=0, padx="5")
num1 = Entry(root)
num1.grid(row=0, column=1, padx="5", pady="5")

label_num1 = Label(root, text="Enter the second number/measurement:")
label_num1.grid(row=1, column=0, padx="5")
num2 = Entry(root)
num2.grid(row=1, column=1, padx="5", pady="5")

calc_btn = Button(root, text="Calculate", command=call_calc)
calc_btn.grid(row=2, column=1)

quit_btn = Button(root, text="Quit", command=quitter)
quit_btn.grid(row=10, column=2, padx="5", pady="5")

root.mainloop()
