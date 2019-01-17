from tkinter import *

root = Tk()
root.minsize(720, 480)
root.title("Toastmeister v2004")


def leftClick(*args):
    print("Left")


def middleClick(*args):
    print("Middle")


def rightClick(*args):
    print("Right")


root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", middleClick)
root.bind("<Button-3>", rightClick)

root.mainloop()