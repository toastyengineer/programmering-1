from tkinter import *

root = Tk()
root.minsize(720, 480)
root.maxsize(720,480)
root.title("Toastmeister v2005")



btnquit = Button(root, text="Quit", bg="red", command=exit)
btnquit.pack(side=LEFT, fill=Y)


root.mainloop()