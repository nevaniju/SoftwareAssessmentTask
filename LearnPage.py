import tkinter as tk
from PIL import Image, ImageTk

class Page2:
    def __init__(self):
        # Create a new root window for page 2
        self.root = tk.Tk()
        self.root.title("Learn Page")
        self.root.geometry("500x700")
        self.root.configure(bg="#FFA500")
        self.root.resizable(False, False)


        # Create a frame with an orange border
        border_frame = tk.Frame(self.root, bg="#FFE2CF", bd=5)
        border_frame.place(relx=0.5, rely=0.5, anchor="center", width=470, height=680)

        # Create a title label
        title_label = tk.Label(border_frame, text="Learn!", font=("Helvetica", 48, "bold"), fg="#D2691E", bg="#FFE2CF")
        title_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        # Create a label for the rectangle section
        rectangle_label = tk.Label(border_frame, text="To find the area of a rectangle, you\nmultiply the length of the rectangle by the width.", font=("Helvetica", 16), bg="#FFE2CF", fg="#D2691E", justify="left")
        rectangle_label.place(x=20, y=100)

        # Rectangle area formula
        rectangle_formula = tk.Label(border_frame, text="Area = Length x Width", font=("Helvetica", 18, "bold"), bg="#FFE2CF", fg="#D2691E")
        rectangle_formula.place(x=20, y=160)

        # Create an image of a rectangle
        rectangle_image_file = "rectanglearea.png"
        rectangle_image = Image.open(rectangle_image_file)
        rectangle_image = rectangle_image.resize((150, 70))
        rectangle_photo = ImageTk.PhotoImage(rectangle_image)
        rectangle_image_label = tk.Label(border_frame, image=rectangle_photo, bg="#FFE2CF")
        rectangle_image_label.image = rectangle_photo
        rectangle_image_label.place(x=300, y=120)

        # Create a label for the triangle section
        triangle_label = tk.Label(border_frame, text="To find the area of a triangle, you\nmultiply the length by the width\nand divide your answer by 2.", font=("Helvetica", 16), bg="#FFE2CF", fg="#D2691E", justify="left")
        triangle_label.place(x=20, y=240)

        # Triangle area formula
        triangle_formula = tk.Label(border_frame, text="Area = Length x Width x 1/2", font=("Helvetica", 18, "bold"), bg="#FFE2CF", fg="#D2691E")
        triangle_formula.place(x=20, y=320)

        # Create an image of a triangle
        triangle_image_file = "trianglearea.png"
        triangle_image = Image.open(triangle_image_file)
        triangle_image = triangle_image.resize((150, 100))
        triangle_photo = ImageTk.PhotoImage(triangle_image)
        triangle_image_label = tk.Label(border_frame, image=triangle_photo, bg="#FFE2CF")
        triangle_image_label.image = triangle_photo
        triangle_image_label.place(x=300, y=260)

        # Create a label for the square section
        square_label = tk.Label(border_frame, text="To find the area of a square, you\nmultiply the given side by itself.", font=("Helvetica", 16), bg="#FFE2CF", fg="#D2691E", justify="left")
        square_label.place(x=20, y=400)

        # Square area formula
        square_formula = tk.Label(border_frame, text="Area = Side²", font=("Helvetica", 18, "bold"), bg="#FFE2CF", fg="#D2691E")
        square_formula.place(x=20, y=460)

        # Create an image of a square
        square_image_file = "squarearea.png"
        square_image = Image.open(square_image_file)
        square_image = square_image.resize((150, 140))
        square_photo = ImageTk.PhotoImage(square_image)
        square_image_label = tk.Label(border_frame, image=square_photo, bg="#FFE2CF")
        square_image_label.image = square_photo
        square_image_label.place(x=300, y=420)

        # Add Home Page and Quiz buttons
        home_button = tk.Button(border_frame, text="Home Page", font=("Helvetica", 16), bg="#FFE2CF", fg="#D2691E", relief="flat")
        home_button.place(x=90, y=600, width=150, height=40)

        quiz_button = tk.Button(border_frame, text="Quiz", font=("Helvetica", 16), bg="#FFE2CF", fg="#D2691E", relief="flat")
        quiz_button.place(x=260, y=600, width=150, height=40)

        # Start the tkinter event loop
        self.root.mainloop()

# Create an instance of the Page2 class to run the program
if __name__ == "__main__":
    Page2()
