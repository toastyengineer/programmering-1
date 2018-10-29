from tkinter import *

root = Tk()
root.title("Toastmeister v2001")
root.minsize(720, 480)

def printName():
    print("Hello my name is Eminem.")

button1 = Button(root, text="Print Name", command=printName)
button1.pack()

root.mainloop()