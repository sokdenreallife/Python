# Using Icons, Images, and Exit Buttons
from tkinter import *
from PIL import ImageTk, Image

# This is class & display on the screen
screen = Tk()
screen.title("My app")

# Create function
def button_back():
    return

def button_back():
    return

def button_back():
    return

# Put image icon to app, SUPPORT .ico files
screen.iconbitmap("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\icon.ico")

# Put the background iamge .jpg or .png
my_img1 = ImageTk.PhotoImage(Image.open("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\M1.jpg"))

#image_list = [my_img1, my_img2, my_img3, my_img4]

# My label
my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

# Quit program
button_back = Button(screen, text = "<<", padx = 50, pady = 10, command = button_back)
button_quit = Button(screen, text = "Quit Button", padx = 100, pady = 10, command = screen.quit)
button_forword = Button(screen, text = ">>", padx = 50, pady = 10, command = lambda: button_forword)

# Display on screen
button_back.grid(row = 10, column = 0)
button_quit.grid(row = 10, column = 1)
button_forword.grid(row = 10, column = 2)

# Run in Loop
screen.mainloop()