from tkinter import *

root = Tk()

# Create label widget
myLabel1 = Label(root, text=("Hello World!"))
myLabel2 = Label(root, text=("Hello Cambodia"))

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)

# Run program in loop
root.mainloop()