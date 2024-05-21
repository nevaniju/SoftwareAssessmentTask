import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.configure(background="#FFE2CF", borderwidth= "5px")

        self.title_label = tk.Label(self, text="Area!", font=("Arial", 24), bg="#FFE2CF")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.learn_button = tk.Button(self, text="Learn", font=("Arial", 16), bg="#FFE2CF", activebackground="#FFE2CF")
        self.learn_button.place(relx=0.5, rely=0.3, anchor="center")

        self.quiz_button = tk.Button(self, text="Quiz", font=("Arial", 16), bg="#FFE2CF", activebackground="#FFE2CF")
        self.quiz_button.place(relx=0.5, rely=0.45, anchor="center")

        self.area_calculator_button = tk.Button(self, text="Area Calculator", font=("Arial", 16), bg="#FFA07A", activebackground="#FF7A50")
        self.area_calculator_button.place(relx=0.5, rely=0.6, anchor="center")

        image = Image.open("triangleface.jpg")
        resized_image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(resized_image)
        label = tk.Label(self, image=photo, bg="#FFE2CF")
        label.image = photo
        label.place(relx=0.5, rely=0.8, anchor="center")

if __name__ == "__main__":
    app = Application()
    app.mainloop()