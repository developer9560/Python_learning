from tkinter import *

#label is a widget that is used to display text or images on the screen. It is a simple way to show information to the user. Labels can be used to display static text, such as instructions or messages, or they can be used to display dynamic information, such as the result of a calculation.

windows = Tk()

windows.geometry("600x400") # set window size
windows.title("My Second GUI for making label") # set window titl
windows.configure(bg="lightblue") # set window background color

label = Label(windows,
            text="Hello, Tkinter! ",
            font=("Arial", 24),
            bg="lightblue",
            fg="black",
            bd=2, # border width
            relief=SUNKEN, # border style
            padx=10, # padding x-axis
            pady=10, # padding y-axis
            #anchor="w", # anchor position
            justify="left", # text justification
           # wraplength=200, # wrap text after this length
            image=None, # image to display
            #compound="top", # position of image relative to text
            )
label.pack() # pack the label into the window with some padding
#label.place(x=100, y=100) # place the label at a specific position in the window
# label.grid(row=0, column=0) # place the label in a grid layout

windows.mainloop()