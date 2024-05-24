import tkinter as tk

class Page4:
   def __init__(self):
       # create a new root window for page 4
       self.root = tk.Tk()
       self.root.title("Area Calculator")
       self.root.geometry("500x700")
       self.root.configure(bg="#FFE2CF", highlightbackground="#FFA500", highlightthickness=10)

      
       # Create a title label
       title_label = tk.Label(self.root, text="Area!", font=("Helvetica", 50, "bold"), fg="#D2691E", bg="#FFE2CF")
       title_label.pack(pady=(20, 10))

       subheading_label = tk.Label(self.root, text="Please select your shape", font=("Helvetica", 20), fg="#D2691E", bg="#FFE2CF")
       subheading_label.pack(pady=(0, 20))
      
       # Shape selection
       self.shape_var = tk.StringVar(value="none")
       self.shape_frame = tk.Frame(self.root, bg="#FFE2CF")
       self.shape_frame.pack(pady=(10, 20))
       
       self.rectangle_radio = tk.Radiobutton(self.shape_frame, text="Rectangle", variable=self.shape_var, value="rectangle", command=self.update_form, font=("Helvetica", 18), bg="#FFA500", selectcolor="#A23400", indicatoron=0, width=10,)
       self.square_radio = tk.Radiobutton(self.shape_frame, text="Square", variable=self.shape_var, value="square", command=self.update_form, font=("Helvetica", 18), bg="#FFA500", selectcolor="#A23400", indicatoron=0, width=10,)
       self.triangle_radio = tk.Radiobutton(self.shape_frame, text="Triangle", variable=self.shape_var, value="triangle", command=self.update_form, font=("Helvetica", 18), bg="#FFA500", selectcolor="#A23400", indicatoron=0, width=10)
       
       self.rectangle_radio.grid(row=0, column=0, padx=10, pady=5)
       self.square_radio.grid(row=1, column=0, padx=10, pady=5)
       self.triangle_radio.grid(row=2, column=0, padx=10, pady=5)
      
       # Input fields
       self.form_frame = tk.Frame(self.root, bg="#FFE2CF")
       self.form_frame.pack(pady=20)
      
       self.length_label = tk.Label(self.form_frame, text="Length:", font=("Helvetica", 18), bg="#FFE2CF", fg="#FFA500")
       self.length_entry = tk.Entry(self.form_frame, font=("Helvetica", 18), width=10, fg="#FFDA95")
      
       self.width_label = tk.Label(self.form_frame, text="Width:", font=("Helvetica", 18), bg="#FFE2CF", fg="#FFA500")
       self.width_entry = tk.Entry(self.form_frame, font=("Helvetica", 18), width=10, fg="#FFDA95")
      
       self.side_label = tk.Label(self.form_frame, text="Side Length:", font=("Helvetica", 18), bg="#FFE2CF", fg="#FFA500")
       self.side_entry = tk.Entry(self.form_frame, font=("Helvetica", 18), width=10, fg="#FFDA95")
      
       self.base_label = tk.Label(self.form_frame, text="Base:", font=("Helvetica", 18), bg="#FFE2CF", fg="#FFA500")
       self.base_entry = tk.Entry(self.form_frame, font=("Helvetica", 18), width=10, fg="#FFDA95")
      
       self.height_label = tk.Label(self.form_frame, text="Height:", font=("Helvetica", 18), bg="#FFE2CF", fg="#FFA500")
       self.height_entry = tk.Entry(self.form_frame, font=("Helvetica", 18), width=10, fg="#FFDA95")
       
       self.calculate_button = tk.Button(self.root, text="Calculate Area", command=self.calculate_area, font=("Helvetica", 18, "bold"), bg="#FFE2CF", fg="#FFA500", activebackground="#FFA500", activeforeground="#FFE2CF", width=15, bd=0, highlightthickness=0)
       self.calculate_button.pack(pady=20)
      
       self.result_label = tk.Label(self.root, text="", font=("Helvetica", 22), bg="#FFE2CF")
       self.result_label.pack(pady=20)
       
       self.home_button = tk.Button(self.root, text="Home Page", font=("Helvetica", 18, "bold"), bg="#FFE2CF", fg="#FFA500", activebackground="#FF8C00", activeforeground="#FFA500", width=10, bd=0, highlightthickness=0)
       self.home_button.pack(side=tk.LEFT, padx=50, pady=10)
       
       self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_fields, font=("Helvetica", 18, "bold"), bg="#FFE2CF", fg="#FFA500", activebackground="#FF8C00", activeforeground="#FFA500", width=10, bd=0, highlightthickness=0)
       self.clear_button.pack(side=tk.RIGHT, padx=50, pady=10)

       # Initialize the form with the default shape
       self.update_form()

   def update_form(self):
       # Clear the current form
       for widget in self.form_frame.winfo_children():
           widget.grid_forget()
      
       # Display the appropriate input fields based on the selected shape
       shape = self.shape_var.get()
       if shape == "rectangle":
           
           self.length_label.grid(row=0, column=0, pady=5, padx=5)
           self.length_entry.grid(row=0, column=1, pady=5, padx=5)
           self.width_label.grid(row=1, column=0, pady=5, padx=5)
           self.width_entry.grid(row=1, column=1, pady=5, padx=5)
       elif shape == "square":
           self.side_label.grid(row=0, column=0, pady=5, padx=5)
           self.side_entry.grid(row=0, column=1, pady=5, padx=5)
       elif shape == "triangle":
           self.base_label.grid(row=0, column=0, pady=5, padx=5)
           self.base_entry.grid(row=0, column=1, pady=5, padx=5)
           self.height_label.grid(row=1, column=0, pady=5, padx=5)
           self.height_entry.grid(row=1, column=1, pady=5, padx=5)
      
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
      
   def clear_fields(self):
       for entry in [self.length_entry, self.width_entry, self.side_entry, self.base_entry, self.height_entry]:
           entry.delete(0, tk.END)
       self.result_label.config(text="")
      
   def run(self):
       # start the Tkinter event loop
       self.root.mainloop()

# To run the application
if __name__ == "__main__":
   app = Page4()
   app.run()
