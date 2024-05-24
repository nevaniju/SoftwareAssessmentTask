import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk


class Page2:
    def __init__(self):
        # create a new root window for page 2
        self.root = tk.Tk()
        self.root.title("Learn Page")
        self.root.geometry("500x700")
        self.root.configure(bg="#FFA500")

        # Create a frame
        border_frame = tk.Frame(self.root, bg="#FFE2CF", bd=10)
        border_frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=680)


        # create a title label
        title_label = tk.Label(self.root, text="Learn!", font=("Helvetica", 42, "bold"), fg="#D2691E", bg="#FFE2CF")
        title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # create a label for the rectangle section
        rectangle_label = tk.Label(self.root, text="Rectangle", font=("Helvetica", 24, "bold"), bg="#FFE2CF", fg="#D2691E")
        rectangle_label.place(x=20, y=100)

        # create a label for the area formula
        area_label = tk.Label(self.root, text="To find the area of a rectangle, you multiply the length of the rectangle by the width.", font=("Helvetica", 14), wraplength=250, bg="#FFE2CF", fg="#D2691E")
        area_label.place(x=20, y=140)

        # create an image of a rectangle
        rectangle_image_file = "rectanglearea.png"
        rectangle_image = Image.open(rectangle_image_file)
        rectangle_image = rectangle_image.resize((160, 140))
        rectangle_photo = ImageTk.PhotoImage(rectangle_image)
        rectangle_image_label = tk.Label(self.root, image=rectangle_photo, bg="#FFE2CF")
        rectangle_image_label.image = rectangle_photo
        rectangle_image_label.place(x=300, y=100)

        # create a label for the square section
        triangle_label = tk.Label(self.root, text="Triangle", font=("Helvetica", 24, "bold"), bg="#FFE2CF", fg="#D2691E")
        triangle_label.place(x=20, y=280)

        # create a label for the area formula
        area_label = tk.Label(self.root, text="To find the area of a triangle, you multiply the base by the height and divide your answer by 2.", font=("Helvetica", 14), wraplength=250, bg="#FFE2CF", fg="#D2691E")
        area_label.place(x=20, y=320)

        # Create an image of a triangle
        triangle_image_file = "trianglearea.png"
        triangle_image = Image.open(triangle_image_file)
        triangle_image = triangle_image.resize((150, 150))
        triangle_photo = ImageTk.PhotoImage(triangle_image)
        triangle_image_label = tk.Label(self.root, image=triangle_photo, bg="#FFE2CF")
        triangle_image_label.image = triangle_photo
        triangle_image_label.place(x=300, y=280)


        # Create a label for the square section
        square_label = tk.Label(self.root, text="Square", font=("Helvetica", 24, "bold"), bg="#FFE2CF", fg="#D2691E")
        square_label.place(x=20, y=460)

        # create a label for the area formula
        area_label = tk.Label(self.root, text="To find the area of a square, you multiply the given side by itself.", font=("Helvetica", 14), wraplength=250, bg="#FFE2CF", fg="#D2691E")
        area_label.place(x=20, y=500)

        # create an image of a circle
        square_image_file = "squarearea.png"
        square_image = Image.open(square_image_file)
        square_image = square_image.resize((150, 140))
        square_photo = ImageTk.PhotoImage(square_image)
        square_image_label = tk.Label(self.root, image=square_photo, bg="#FFE2CF")
        square_image_label.image = square_photo
        square_image_label.place(x=300, y=460)

        # start the tkinter event loop
        self.root.mainloop()