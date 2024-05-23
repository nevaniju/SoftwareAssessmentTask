import tkinter as tk

class Page4:
    def __init__(self):
        # create a new root window for page 4
        self.root = tk.Tk()
        self.root.title("Area Calculator")
        self.root.geometry("500x700")
        self.root.configure(bg="#FFE2CF")
        
        # Shape selection
        self.shape_var = tk.StringVar(value="rectangle")
        self.shape_frame = tk.Frame(self.root, bg="#FFE2CF")
        self.shape_frame.pack(pady=20)
        
        self.rectangle_radio = tk.Radiobutton(self.shape_frame, text="Rectangle", variable=self.shape_var, value="rectangle", command=self.update_form, font=("Helvetica", 14), bg="#faf0be")
        self.square_radio = tk.Radiobutton(self.shape_frame, text="Square", variable=self.shape_var, value="square", command=self.update_form, font=("Helvetica", 14), bg="#faf0be")
        self.triangle_radio = tk.Radiobutton(self.shape_frame, text="Triangle", variable=self.shape_var, value="triangle", command=self.update_form, font=("Helvetica", 14), bg="#faf0be")
        
 
        
        self.length_label = tk.Label(self.form_frame, text="Length:", font=("Helvetica", 14), bg="#FFE2CF")
        self.length_entry = tk.Entry(self.form_frame, font=("Helvetica", 14))
        
        self.width_label = tk.Label(self.form_frame, text="Width:", font=("Helvetica", 14), bg="#FFE2CF")
        self.width_entry = tk.Entry(self.form_frame, font=("Helvetica", 14))
        
        self.side_label = tk.Label(self.form_frame, text="Side Length:", font=("Helvetica", 14), bg="#FFE2CF")
        self.side_entry = tk.Entry(self.form_frame, font=("Helvetica", 14))
        
        self.base_label = tk.Label(self.form_frame, text="Base:", font=("Helvetica", 14), bg="#FFE2CF")
        self.base_entry = tk.Entry(self.form_frame, font=("Helvetica", 14))
        
        self.height_label = tk.Label(self.form_frame, text="Height:", font=("Helvetica", 14), bg="#FFE2CF")
        self.height_entry = tk.Entry(self.form_frame, font=("Helvetica", 14))
        

        

    def calculate_area(self):
        shape = self.shape_var.get()
        try:
            if shape == "rectangle":
                length = float(self.length_entry.get())
                width = float(self.width_entry.get())
                area = length * width
                self.result_label.config(text=f"Area of Rectangle: {area}")
            elif shape == "square":
                side = float(self.side_entry.get())
                area = side ** 2
                self.result_label.config(text=f"Area of Square: {area}")
            elif shape == "triangle":
                base = float(self.base_entry.get())
                height = float(self.height_entry.get())
                area = 0.5 * base * height
                self.result_label.config(text=f"Area of Triangle: {area}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")
        
    def run(self):
        # start the Tkinter event loop
        self.root.mainloop()

# To run the application
if __name__ == "__main__":
    app = Page4()
    app.run()
