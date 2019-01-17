from tkinter import *


class yeet:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked")

root = Tk()
root.minsize(720, 480)
root.title("Toastmeister v2002")

b = yeet(root)

root.mainloop()