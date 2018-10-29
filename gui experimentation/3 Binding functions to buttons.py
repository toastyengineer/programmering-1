from tkinter import *

root = Tk()
root.title("Toastmeister v2003")
root.minsize(720, 480)


def printname():
    print("Hello my name is Eminem.")


button1 = Button(root, text="Print Name", command=printname)
button1.pack()

root.mainloop()