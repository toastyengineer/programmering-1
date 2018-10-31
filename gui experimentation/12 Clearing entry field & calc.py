from tkinter import *
import tkinter.messagebox

def show_answer(*args):
    if num1.get().isalpha() or num2.get().isalpha():
        tkinter.messagebox.showwarning("Error","Invalid input, can only be integers.")
    elif num1.get() == "" or num2.get() == "":
        tkinter.messagebox.showwarning("Error", "Nothing was entered.")
    else:
        Ans = int(num1.get()) + int(num2.get())
        sum.delete(0, "end")
        sum.insert(0, Ans)


root = Tk()

Label(root, text="Number 1:").grid(row=0)
Label(root, text="Number 2:").grid(row=1)
Label(root, text="Sum:").grid(row=2)

num1 = Entry(root)
num1.bind("<Return>", show_answer)
num1.grid(row=0, column=1)

num2 = Entry(root)
num2.bind("<Return>", show_answer)
num2.grid(row=1, column=1)

sum = Entry(root)
sum.grid(row=2, column=1)

Button(root, text='Exit', command=root.quit).grid(row=4, column=0, sticky=W, pady=4, padx=4)
Button(root, text='Calculate', command=show_answer).grid(row=4, column=1, pady=4)

root.mainloop()