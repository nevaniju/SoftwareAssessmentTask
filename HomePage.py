import tkinter as tk

root = tk.Tk()
root.title("Area Calculator")
root.geometry("400x600")
root.configure(bg="#faf0be")

# Create a frame for the title and buttons
title_frame = tk.Frame(root, bg="#faf0be")
title_frame.pack(pady=20)

# Create the title label
title_label = tk.Label(title_frame, text="Area!", font=("Helvetica", 24, "bold"), bg="#faf0be")
title_label.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#faf0be")
button_frame.pack(pady=20)

# Create the learn button
learn_button = tk.Button(button_frame, text="Learn", bg="#cfe3f7", font=("Helvetica", 16), command=lambda: print("Learn button clicked"))
learn_button.grid(row=0, column=0, padx=20)

# Create the quiz button
quiz_button = tk.Button(button_frame, text="Quiz", bg="#cfe3f7", font=("Helvetica", 16), command=lambda: print("Quiz button clicked"))
quiz_button.grid(row=0, column=1, padx=20)

# Create the area calculator button
area_button = tk.Button(button_frame, text="Area Calculator", bg="#cfe3f7", font=("Helvetica", 16), command=lambda: print("Area calculator button clicked"))
area_button.grid(row=0, column=2, padx=20)

root.mainloop()