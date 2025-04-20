from tkinter import *

count = 0 # global variable to keep track of the number of clicks
def click_button():
    global count # use the global variable count
    count += 1 # increment the count by 1
    print(f"Button clicked {count} times!") # print the number of clicks
    label.config(text=f" {count} ") # update the label with the number of clicks
    # This function will be called when the button is clicked


windows = Tk()
windows.geometry("600x400") # set window size
windows.title("My Third GUI for making button") # set window title
windows.configure(bg="lightblue") # set window background color
button = Button(windows,
                text="Click Me!",
                font=("Arial", 12),
                bg="red",
                fg="black",
                bd=2, # border width
                relief=SUNKEN, # border style
                padx=10, # padding x-axis
                pady=10, # padding y-axis
                activebackground="green", # background color when button is clicked
                )

button.config(command=click_button) # set the command to be executed when the button is clicked
#button.bind("<Button-1>", lambda event: click_button()) # bind left mouse button click to the function

label = Label(windows,text=count, font=("Arial", 24), bg="lightblue", fg="black")
label.pack() # pack the label into the window with some padding 
button.pack() # pack the button into the window with some padding

windows.mainloop()