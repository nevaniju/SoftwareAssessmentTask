from tkinter import *
root = Tk() 
root.title("Learning Area") #change the window title
root.geometry("400x400") #change the window size, x and y coordinates
root.configure(bg="lightgray") #set the background of the window
from tkinter import * # imports all symbols from the tkinter module into the current name space

Label1=Label(root,text="Area!") 
Label1.pack(pady=20) 

root.mainloop()