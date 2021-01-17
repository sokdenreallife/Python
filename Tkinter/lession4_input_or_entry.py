from tkinter import *

root = Tk()

# Create Entry
e = Entry(root, width = 50, bg = "white", fg = "black", borderwidth = 5)
e.pack()
e.insert(0, "Enter your name")

# Create function
def myClick():

#    myLabel = Label(root, text = "Hello " + e.get())

    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

myBotton = Button(root, text = "Enter Your Name: ", padx = 50, command = myClick, fg = "blue", bg = "#ffffff")

# Showing onto the screen
myBotton.pack()

# Run in Loop
root.mainloop()