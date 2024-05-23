import tkinter as tk
import LearnPage
import QuizPage
import AreaCalculatorPage
from PIL import Image, ImageTk

def navigate_to_learnpage():
    # destroy the current page
    root.destroy()

    # create a new instance of page 2
    page2_instance = LearnPage.Page2()

def navigate_to_quizpage():
    # destroy the current page
    root.destroy() 
    quiz_root = tk.Tk()
    quiz_page = QuizPage.Page3(quiz_root)
    quiz_root.mainloop()

    # create a new instance of page 3
    page3_instance = QuizPage.Page3()

def navigate_to_areacalculatorpage():
    # destroy the current page
    root.destroy()

    # create a new instance of page 4
    page4_instance = AreaCalculatorPage.Page4()

# create the root window for page 1
root = tk.Tk()
root.title("Area!")
root.geometry("500x700")
root.configure(bg="#FFE2CF")

# create a title label
title_label = tk.Label(root, text="Area!", font=("Helvetica", 36, "bold"), fg="red", bg="#FFE2CF")
title_label.grid(row=0, column=0, columnspan=2, pady=(50, 20), padx=(50, 50))

# create a button that navigates to page 2
button2 = tk.Button(root, text="Learn", command=navigate_to_learnpage, font=("Helvetica", 24), bg="orange", fg="black", width=8, height=1)
button2.grid(row=1, column=0, pady=(0, 20), padx=(50, 50))

# create a button that navigates to page 3
button3 = tk.Button(root, text="Quiz", command=navigate_to_quizpage, font=("Helvetica", 24), bg="orange", fg="black", width=8, height=1)
button3.grid(row=1, column=1, pady=(0, 20), padx=(50, 50))

# create a button that navigates to page 4
button4 = tk.Button(root, text="Area Calculator", command=navigate_to_areacalculatorpage, font=("Helvetica", 24), bg="orange", fg="black", width=18, height=1)
button4.grid(row=2, column=0, columnspan=2, pady=(0, 50), padx=(50, 50))

# create an image under the buttons
image_file = "multipleshapes.png" 
image = Image.open(image_file)
image = image.resize((350, 250))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg="#faf0be")
image_label.grid(row=3, column=0, columnspan=2, pady=(0, 50), padx=(50, 50))

# center the widgets in the window
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

# start the Tkinter event loop
root.mainloop()