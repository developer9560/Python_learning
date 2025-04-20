from tkinter import *


window = Tk()

window.geometry("600x400") # set window size
window.title("My First GUI") # set window title
window.configure(bg="lightblue") # set window background color
 

window.mainloop() #place window on screen and wait for user to close it , listen for events
# window.mainloop() is a blocking call, meaning it will not return until the window is closed.
