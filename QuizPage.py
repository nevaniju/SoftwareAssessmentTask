import tkinter as tk

class Page3:
    def __init__(self):
        # create a new root window for page 2
        self.root = tk.Tk()
        self.root.title("Quiz Page")
        self.root.geometry("500x700")
        self.root.configure(bg="#faf0be")
        

        # add widgets to page 2 here
        label = tk.Label(self.root, text="Quiz!")
        label.pack()

    def run(self):
        # start the Tkinter event loop
        self.root.mainloop()