import tkinter as tk


root = tk.Tk()
root.geometry("400x600")
root.configure(bg="#FFB9B9", bd=10, relief="solid", highlightcolor="#FF5252")  # Add a border and set its color
root.resizable(False,False) #make the window non resizable

# Create a title label
title_label = tk.Label(root, text="Area!", font=("Helvetica Neue", 32, "bold"), fg="#FF6868", bg="#FFB9B9")

# Add the title label to the window and position it
title_label.place(x=100, y=50)

# Create three buttons
btn_rectangle = tk.Button(root, text="Learn", font=("Helvetica Neue", 18, "bold"), bg="#FFD1D1", fg="#FF5252", bd=1, activebackground="#FFD1D1")  # Change the button color
btn_square = tk.Button(root, text="Quiz", font=("Helvetica Neue", 18, "bold"), bg="#FFD1D1", fg="#FF5252", bd=1, activebackground="#FFD1D1")  # Change the button color
btn_triangle = tk.Button(root, text="Area Calculator", font=("Helvetica Neue", 18, "bold"), bg="#FFD1D1", fg="#FF5252", bd=1, activebackground="#FFD1D1")  # Change the button color

# Add the buttons to the window and position them on top of each other
btn_rectangle.place(x=100, y=150, width=200, height=50)
btn_square.place(x=100, y=210, width=200, height=50)
btn_triangle.place(x=100, y=270, width=200, height=50)


root.mainloop()

