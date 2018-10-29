from tkinter import *


def donothing():
    print("Did nothing")


root = Tk()
root.minsize(720, 480)
root.maxsize(720, 480)
root.title("Toastmeister v2006")

menu = Menu(root)
root.config(menu=menu)

submenu1 = Menu(menu)
menu.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="New Project...", command=donothing)
submenu1.add_separator()
submenu1.add_command(label="Exit", command=exit)

submenu2 = Menu(menu)
menu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Filetype", command=donothing)

submenu2 = Menu(menu)
menu.add_cascade(label="View", menu=submenu2)
submenu2.add_command(label="File types", command=donothing)

submenu3 = Menu(menu)
menu.add_cascade(label="Navigate", menu=submenu3)
submenu3.add_command(label="Class...", command=donothing)


root.mainloop()