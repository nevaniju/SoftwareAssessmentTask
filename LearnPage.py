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
        rectangle_label = tk.Label(self.root, text="Rectangle", font=("Helvetica", 24, "bold"), bg="#faf0be")
        rectangle_label.pack(pady=(0, 10))

        # create a label for the area formula
        area_label = tk.Label(self.root, text="To find the area of a rectangle, multiply its length by its width.", font=("Helvetica", 14), bg="#faf0be")
        area_label.pack(pady=(0, 10))

        # create an image of a rectangle
        rectangle_image_file = "squarearea.jpeg"  # replace with the path to your image file
        rectangle_image = Image.open(rectangle_image_file)
        rectangle_image = rectangle_image.resize((150, 150))  # resize the image to 150x150 pixels
        rectangle_photo = ImageTk.PhotoImage(rectangle_image)
        rectangle_image_label = tk.Label(self.root, image=rectangle_photo, bg="#faf0be")
        rectangle_image_label.image = rectangle_photo
        rectangle_image_label.pack(pady=(0, 20))

        # create a label for the square section
        square_label = tk.Label(self.root, text="Square", font=("Helvetica", 24, "bold"), bg="#faf0be")
        square_label.pack(pady=(0, 10))

        # create a label for the area formula
        area_label = tk.Label(self.root, text="To find the area of a square, square its side length.", font=("Helvetica", 14), bg="#faf0be")
        area_label.pack(pady=(0, 10))

        # create an image of a square
        square_image_file = "squarearea.jpeg"  # replace with the path to your image file
        square_image = Image.open(square_image_file)
        square_image = square_image.resize((150, 150))  # resize the image to 150x150 pixels
        square_photo = ImageTk.PhotoImage(square_image)
        square_image_label = tk.Label(self.root, image=square_photo, bg="#faf0be")
        square_image_label.image = square_photo
        square_image_label.pack(pady=(0, 20))

        # create a label for the circle section
        circle_label = tk.Label(self.root, text="Circle", font=("Helvetica", 24, "bold"), bg="#faf0be")
        circle_label.pack(pady=(0, 10))

        # create a label for the area formula
        area_label = tk.Label(self.root, text="To find the area of a circle, square its radius and multiply by pi.", font=("Helvetica", 14), bg="#faf0be")
        area_label.pack(pady=(0, 10))

        # create an image of a circle
        circle_image_file = "squarearea.jpeg"  # replace with the path to your image file
        circle_image = Image.open(circle_image_file)
        circle_image = circle_image.resize((150, 150))  # resize the image to 150x150 pixels
        circle_photo = ImageTk.PhotoImage(circle_image)
        circle_image_label = tk.Label(self.root, image=circle_photo, bg="#faf0be")
        circle_image_label.image = circle_photo
        circle_image_label.pack(pady=(0, 50))

        # create a back button
        back_button = tk.Button(self.root, text="Back", font=("Helvetica", 18), bg="#faf0be", fg="red", command=self.root.destroy)
        back_button.pack(pady=(0, 20))

        # start the tkinter event loop
        self.root.mainloop()