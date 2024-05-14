import tkinter as tk

def show_page_two():
    page_one.forget()
    page_two.lift()

root = tk.Tk()
root.geometry("400x600")
root.configure(bg="#FFE5E5", relief="solid", highlightcolor="#FF5252", highlightthickness=5)  # Add a border and set its color and thickness
root.resizable(False,False) #make the window non resizable

# Create a title label
title_label = tk.Label(root, text="Area!", font=("Helvetica Neue", 32, "bold"), fg="#FF5252", bg="#FFB9B9")

# Add the title label to the window and position it 
title_label.pack(pady=(50, 50))

# Create frames for the pages
page_one = tk.Frame(root, bg="#FFD1D1")
page_two = tk.Frame(root, bg="#FFD1D1")


# Create three buttons in the first frame
btn_rectangle = tk.Button(page_one, text="Learn", font=("Helvetica Neue", 18, "bold"), bg="#FF5252", fg="white", bd=0, command=show_page_two)
btn_square = tk.Button(page_one, text="Quiz", font=("Helvetica Neue", 18, "bold"), bg="#FF5252", fg="white", bd=0)
btn_triangle = tk.Button(page_one, text="Area Calculator", font=("Helvetica Neue", 18, "bold"), bg="#FF5252", fg="white", bd=0)

# Add the buttons to the first frame and position them in the center
btn_rectangle.pack(pady=(0, 20))
btn_square.pack(pady=(0, 20))
btn_triangle.pack(pady=(0, 20))

# Add a label to the second frame
page_two_label = tk.Label(page_two, text="Page Two", font=("Helvetica Neue", 24, "bold"), fg="#FF5252", bg="#FFD1D1")

# Add the label to the second frame and position it in the center
page_two_label.pack(pady=(100, 100))

# Add the frames to the window
page_one.pack(fill="both", expand=True)

root.mainloop()