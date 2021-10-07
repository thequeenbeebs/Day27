# GRAPHICAL USER INTERFACES WITH TKINTER AND FUNCTIONAL ARGUMENTS

# History of GUI and Introduction to Tkinter
#   Huge in the 90's - before that you had to use a CLI
#   GUIs allowed a user to point and click on the screen
#   Tkinter - a way to create your own GUI

# Creating Windows and Labels with Tkinter

from tkinter import *

def button_clicked():
    print("I got clicked")
    text = inp.get()
    my_label.config(text=text)


# Creates a window
window = Tk()
# Changes window title
window.title('My First GUI Program')
# Window size
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Create a label w/text and font
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

# Setting Default Values for Optional Arguments Inside a Function Header
#   Advanced Python Arguments - to specify a wider range of inputs
#   Keyword Arguments my_func(a=3, c=2, b=1)
#   Arguments with Default Values: you only need to add arguments for ones that won't be default


def my_function(a=1, b=2, c=3):
    print(a + b + c)

# *args: Many Positional Arguments
#   Unlimited Arguments: * tells Python it can accept any number of arguments, then loop through


def add(*args):
    for n in args:
        print(n)


# **kwargs: Many Keyword Arguments
#   Tkinter uses keyword arguments

# Buttons, Entry, and Setting Component Options
my_label['text'] = "New Text"
my_label.config(text="New Text")
# Places in top left corner
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry - an input
inp = Entry(width=10)
inp.grid(column=3, row=2)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Other Tkinter Widgets: Radio buttons, Scales, Check buttons, and More
# Text
# Spinbox
# Scale
# Checkbox
# Radio button
# Listbox

# Tkinter Layout Managers: pack(), place(), and grid()
#   Pack - packs each widget next to each other, by default top down
#   Place - precise positioning
#   Grid - divide program into columns and rows
#   You cannot mix grid and pack in the same function!

# Keeps window on screen, end of code
window.mainloop()
