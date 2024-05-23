import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import LearnPage
import QuizPage
import AreaCalculatorPage


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
root.configure(bg="#FFA500")
root.resizable(False, False)

# Create a frame
border_frame = tk.Frame(root, bg="#FFE2CF", bd=10)
border_frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=680)


# create a title label
title_label = tk.Label(root, text="Area!", font=("Helvetica", 50, "bold"), fg="#D2691E", bg="#FFE2CF")
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# create a button that navigates to page 2
button2 = ctk.CTkButton(border_frame, text="Learn!", command=navigate_to_learnpage, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=200, height=50)
button2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# create a button that navigates to page 3
button3 = ctk.CTkButton(border_frame, text="Quiz!", command=navigate_to_quizpage, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=200, height=50)
button3.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# create a button that navigates to page 4
button4 = ctk.CTkButton(border_frame, text="Area Calculator", command=navigate_to_areacalculatorpage, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=200, height=50)
button4.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# create an image under the buttons
image_file = "multipleshapes.png" 
image = Image.open(image_file)
image = image.resize((400, 250))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg="#FFE2CF")
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