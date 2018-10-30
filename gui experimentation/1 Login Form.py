from tkinter import *
import tkinter.messagebox

user1 = "root"
pass1 = "password"


def confirm_exit():
    answer = tkinter.messagebox.askquestion("Info", "Are you sure you want to cancel?")
    if answer == "yes":
        exit()


def log_in():
    if entry_user.get() == user1 and entry_pass.get() == pass1:
        tkinter.messagebox.showinfo("Info", "Successfully logged in!")
    elif entry_user.get() == "" or entry_pass.get() == "":
        tkinter.messagebox.showinfo("Info", "You did not enter a valid password and/or username.")
    else:
        tkinter.messagebox.showwarning("Warning", "Entered username or password was incorrect.\nIs caps-lock disabled?")


def register():
    tkinter.messagebox.showinfo("Info","Registration is currently unavailable")


def checkbox():
    checkbox_state = checky.get()


root = Tk()
root.title("PQ")
root.resizable(False, False)
# Username and Password label
user = Label(root, text="Username: ")
user.grid(row=0, sticky=E)
password = Label(root, text="Password: ")
password.grid(row=1, sticky=E)

# Username and Password entries
entry_user = Entry(root)
entry_user.grid(row=0, column=1)
entry_pass = Entry(root, show='*')
entry_pass.grid(row=1, column=1)

# Checkbox
checky = IntVar()
c = Checkbutton(root, text="Keep me logged in", variable=checky)
c.grid(row=2, columnspan=2)

# Buttons
cancel = Button(root, text="Cancel", command=confirm_exit)
cancel.grid(row=3, column=0, pady=7, padx=10)
register = Button(root, text="Register", command=register)
register.grid(row=3, column=1, pady=7, padx=10)
login = Button(root, text="Login", command=log_in)
login.grid(row=3, column=2, pady=7, padx=10)

root.mainloop()
