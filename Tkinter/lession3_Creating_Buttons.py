from tkinter import *

root = Tk()

# Create function
def myClick():
    myLabel = Label(root, text = "You has been clicked!")
    myLabel.pack()

# Display button click activity (state = DISABLED) 
# (padx = 1, pady = 1) 
# (command = myClick) 
# (fg = "blue") or (fg = "#000000") // foreground color
# (bg = "red") or (bg = "#ffffff") // background color

myBotton = Button(root, text = "Click Button", padx = 50, command = myClick, fg = "blue", bg = "#ffffff")

# Showing onto the screen
myBotton.pack()

# Run in Loop
root.mainloop()