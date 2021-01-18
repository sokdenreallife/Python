# Using Icons, Images, and Exit Buttons
from tkinter import *
from PIL import ImageTk, Image

# This is class & display on the screen
screen = Tk()
screen.title("My app")

# Put image icon to app, SUPPORT .ico files
screen.iconbitmap("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\icon.ico")

# Put the background iamge .jpg or .png
my_img = ImageTk.PhotoImage(Image.open("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\M1.jpg"))
my_label = Label(image = my_img)
my_label.pack()

# Quit program
button_quit = Button(screen, text = "Quit Button", padx = 20, pady = 10, command = screen.quit)
button_quit.pack()

# Run in Loop
screen.mainloop()