from tkinter import *
import tkinter.messagebox

# Made up login credentials
user1 = "root"
pass1 = "password"


def confirm_exit():
    answer = tkinter.messagebox.askquestion("Cancel", "Are you sure you want to cancel?")
    if answer == "yes":
        root.quit()


def log_in(*args):
    if entry_user.get() == user1 and entry_pass.get() == pass1:
        if checkbox():
            tkinter.messagebox.showinfo("Info", "Successfully logged in!\nYou will be kept logged in.")
            print("Super mega secure data")
        else:
            tkinter.messagebox.showinfo("Info", "Successfully logged in!")
            print("Super mega secure data")

    elif entry_user.get() == "" or entry_pass.get() == "":
        tkinter.messagebox.showerror("Error", "You did not enter a valid password and/or username.")
    else:
        tkinter.messagebox.showerror("Error", "Entered username or password was incorrect.\nIs caps-lock disabled?")


def register():
    tkinter.messagebox.showinfo("Info", "Registration is currently unavailable")


def checkbox():
    return checky.get()


root = Tk()
root.title("S8 QT")
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
entry_pass.bind("<Return>", log_in)
entry_pass.grid(row=1, column=1)

# Checkbox
checky = IntVar()
c = Checkbutton(root, text="Keep me logged in", variable=checky)
c.grid(row=2, columnspan=2)

# Buttons
cancel = Button(root, text="Cancel", command=confirm_exit).grid(row=3, column=0, pady=7, padx=10)
register = Button(root, text="Register", command=register).grid(row=3, column=1, pady=7, padx=10)
login = Button(root, text="Login", command=log_in).grid(row=3, column=2, pady=7, padx=10)

root.mainloop()
