from tkinter import *


def do_nothing():
    print("Did nothing")


root = Tk()
root.title("Toastmeister v2006")
root.minsize(720,480)
root.maxsize(720,480)

# ***** Drop down *****

menu = Menu(root)
root.config(menu=menu)

submenu1 = Menu(menu)
menu.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="New Project...", command=do_nothing)
submenu1.add_separator()
submenu1.add_command(label="Exit", command=exit)

submenu2 = Menu(menu)
menu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Filetype", command=do_nothing)

submenu2 = Menu(menu)
menu.add_cascade(label="View", menu=submenu2)
submenu2.add_command(label="File types", command=do_nothing)

submenu3 = Menu(menu)
menu.add_cascade(label="Navigate", menu=submenu3)
submenu3.add_command(label="Class...", command=do_nothing)

# ***** Toolbar *****
toolbar = Frame(root, bg="blue")

insertbutton = Button(toolbar, text="Insert Image", command=do_nothing)
insertbutton.pack(side=LEFT, padx=2, pady=2)
printbutton = Button(toolbar, text="Print", command=do_nothing)
printbutton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status bar *****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()