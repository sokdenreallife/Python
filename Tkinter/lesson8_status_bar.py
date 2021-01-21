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

# List
image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(window, text = "Images 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E) # anchor is postion of text, meant (N, NE, E, SE, S, SW, W, NW, OR CENTER) of "sticky" function

# My label
my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

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

    # Update status bar
    status = Label(window, text = "Images " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 11, column = 0, columnspan = 3, sticky = W + E)

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

    # Update status bar
    status = Label(window, text = "Images " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 11, column = 0, columnspan = 3, sticky = W + E)

# Button program
button_back = Button(window, text = "<<", padx = 30, pady = 10, command = back, state = DISABLED)
button_quit = Button(window, text = "Quit Button", padx = 100, pady = 10, command = window.quit)
button_forward = Button(window, text = ">>", padx = 30, pady = 10, command = lambda: forward(2))

# Display position on window app
button_back.grid(row = 10, column = 0)
button_quit.grid(row = 10, column = 1)
button_forward.grid(row = 10, column = 2)
status.grid(row = 11, column = 0, columnspan = 3, sticky = W + E) # "sticky" is postion of text or align in MS. Word

# Run in Loop
window.mainloop()