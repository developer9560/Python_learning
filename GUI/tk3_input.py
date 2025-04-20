from tkinter import *

windows = Tk()

def Submit():
    print(entry.get()) # get the text from the entry widget and print it to the console
   # entry.delete(0, END) # clear the entry widget after submission
    text = entry.get() # get the text from the entry widget 
    label.config(text=text) # update the label with the text from the entry widget
     # clear the entry widget after submission
windows.geometry("600x400") # set window size
windows.title("Take Input from user GUI") # set window title
entry = Entry(windows, width=30, font=("Arial", 12), bg="lightblue", fg="black", bd=2, relief=SUNKEN,)
entry.pack() # pack the entry widget into the window with some padding
button = Button(windows, text="Submit", font=("Arial", 12), bg="red", fg="black", bd=2, relief=SUNKEN, padx=10, pady=10, activebackground="green", 
               # command=lambda: print(entry.get())
               command = Submit # set the command to be executed when the button is clicked
                ) # set the command to be executed when the button is clicked
button.pack() # pack the button into the window with some padding

label = Label(windows ,font=("Arial", 12), bg="lightblue", fg="black")
label.pack() # pack the label into the window with some padding
windows.mainloop() #place window on screen and wait for user to close it , listen for events