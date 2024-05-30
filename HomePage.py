import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import LearnPage
import QuizPage
import AreaCalculatorPage

#set the basic GUI
class Page1:
    def __init__(self, root):
        self.root = root
        self.root.title("Area!")
        self.root.geometry("500x700")
        self.root.configure(bg="#FFA500")
        self.root.resizable(False, False)
        self.create_widgets()

#create the title and the buttons
    def create_widgets(self):
        border_frame = tk.Frame(self.root, bg="#FFE2CF", bd=10)
        border_frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=680)

        title_label = tk.Label(border_frame, text="Area!", font=("Helvetica", 50, "bold"), fg="#D2691E", bg="#FFE2CF")
        title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        button2 = ctk.CTkButton(border_frame, text="Learn!", command=self.navigate_to_learnpage,  font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=200, height=50)
        button2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        button3 = ctk.CTkButton(border_frame, text="Begin Quiz!", command=self.navigate_to_quizpage, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=200, height=50)
        button3.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        button4 = ctk.CTkButton(border_frame, text="Area Calculator", command=self.navigate_to_areacalculatorpage, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=200, height=50)
        button4.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

#image upload for home page
        image_file = "multipleshapes.png" 
        image = Image.open(image_file)
        image = image.resize((375, 250))
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(border_frame, image=photo, bg="#FFE2CF")
        image_label.image = photo
        image_label.grid(row=3, column=0, columnspan=2, pady=(0, 50), padx=(50, 50))

        border_frame.columnconfigure(0, weight=1)
        border_frame.columnconfigure(1, weight=1)
        border_frame.rowconfigure(0, weight=1)
        border_frame.rowconfigure(1, weight=1)
        border_frame.rowconfigure(2, weight=1)
        border_frame.rowconfigure(3, weight=1)

#functions for each of the buttons
    def navigate_to_learnpage(self):
        # destroy the current page
        self.root.destroy()

        # create a new instance of page 2
        page2_instance = LearnPage.Page2()

    def navigate_to_quizpage(self):
        # destroy the current page
        self.root.destroy() 
        quiz_root = tk.Tk()
        quiz_page = QuizPage.Page3(quiz_root)
        quiz_root.mainloop()

        # create a new instance of page 3
        page3_instance = QuizPage.Page3()

    def navigate_to_areacalculatorpage(self):
        # destroy the current page
        self.root.destroy()

        # create a new instance of page 4
        page4_instance = AreaCalculatorPage.Page4()

# start the Tkinter event loop
if __name__ == "__main__":
    root = tk.Tk()
    Page1(root)
    root.mainloop()
