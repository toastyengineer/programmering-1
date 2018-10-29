from tkinter import *
import tkinter.messagebox

#Confirm on exit


def confirm_exit():
    answer = tkinter.messagebox.askquestion("Info", "Are you sure you want to cancel?")
    if answer == "yes":
        exit()


root = Tk()
root.title("PK")
#Username and Password label
user = Label(root, text="Username: ")
user.grid(row=0, sticky=E)
password = Label(root, text="Password: ")
password.grid(row=1, sticky=E)

#Username and Password entries
entry_user = Entry(root)
entry_user.grid(row=0, column=1)
entry_pass = Entry(root)
entry_pass.grid(row=1, column=1)

#Checkbox
c = Checkbutton(root, text="Keep me logged in")
c.grid(row=2, columnspan=2)

#Buttons
login = Button(root, text="Login")
login.grid(row=3, column=1, pady=5, padx=10, sticky=E)
cancel = Button(root, text="Cancel", command=confirm_exit)
cancel.grid(row=3, column=0)

root.mainloop()
