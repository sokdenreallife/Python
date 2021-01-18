# Using Icons, Images, and Exit Buttons
from tkinter import *
from PIL import ImageTk, Image

# This is class & display on the screen
screen = Tk()
screen.title("My app")

# Put image icon to app, SUPPORT .ico files
screen.iconbitmap("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\icon.ico")

# Put the background iamge .jpg or .png
background = ImageTk.PhotoImage(Image.open("background.jpg"))
my_label = Label(image = background)
my_label.pack()

# Quit program
button_quit = Button(screen, text = "Quit Button", padx = 20, pady = 10, command = screen.quit)
button_quit.pack()

# Run in Loop
screen.mainloop()