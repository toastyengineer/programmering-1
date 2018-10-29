from tkinter import *

root = Tk()
root.title("Toastmeister v2010")

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(10, 10, 150, 50, fill="green")

root.mainloop()