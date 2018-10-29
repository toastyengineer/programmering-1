from tkinter import *

root = Tk()
root.minsize(720, 480)
root.title("Toastmeister v2004")


def leftClick(event):
    print("Left")


def middleClick(event):
    print("Middle")


def rightClick(event):
    print("Right")


root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", middleClick)
root.bind("<Button-3>", rightClick)

root.mainloop()