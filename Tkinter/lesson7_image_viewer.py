# Using Icons, Images, and Exit Buttons
from tkinter import *
from PIL import ImageTk, Image

# This is class & display on the window
window = Tk()
window.title("Image Viewer")

# Put image icon to app, SUPPORT .ico files
window.iconbitmap("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\icon.ico")

# Put the background iamge .jpg or .png
my_img1 = ImageTk.PhotoImage(Image.open("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\p1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\p2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\p3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("D:\Cloud Storage\GitHub\Programming Language\Python\Tkinter\images\p4.png"))

# My label
my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

# List
image_list = [my_img1, my_img2, my_img3, my_img4]

# Create function
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_back = Button(window, text = "<<", padx = 30, pady = 10, command = lambda : back(image_number - 1))
    button_forward = Button(window, text = ">>", padx = 30, pady = 10, command = lambda: forward(image_number + 1))

    if image_number == 4:
        button_forward = Button(window, text = ">>", padx = 30, pady = 10, state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 10, column = 0)
    button_forward.grid(row = 10, column = 2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(window, text = ">>", padx = 30, pady = 10, command = lambda: forward(image_number + 1))
    button_back = Button(window, text = "<<", padx = 30, pady = 10, command = lambda : back(image_number - 1))

    if image_number == 1:
        button_back = Button(window, text = "<<", padx = 30, pady = 10, state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 10, column = 0)
    button_forward.grid(row = 10, column = 2)

# Button program
button_back = Button(window, text = "<<", padx = 30, pady = 10, command = back, state = DISABLED)
button_quit = Button(window, text = "Quit Button", padx = 100, pady = 10, command = window.quit)
button_forward = Button(window, text = ">>", padx = 30, pady = 10, command = lambda: forward(2))

# Display on window
button_back.grid(row = 10, column = 0)
button_quit.grid(row = 10, column = 1)
button_forward.grid(row = 10, column = 2)

# Run in Loop
window.mainloop()