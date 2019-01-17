from tkinter import*
import tkinter.messagebox


root = Tk()
root.title("Toastmeister v2009")
root.minsize(720,480)
root.maxsize(720,480)

tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 300 years.")

answer = tkinter.messagebox.askquestion("Question 1", "Do you have two legs?")

if answer == "yes":
    print("8===D~ ")
else:
    print("Too bad.")


root.mainloop()