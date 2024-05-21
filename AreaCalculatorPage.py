import tkinter as tk

class AreaCalculatorPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#faf0be")
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Area Calculator", font=("Helvetica", 24, "bold"), bg="#faf0be", pady=20)
        self.title_label.pack()

        self.rectangle_button = tk.Button(self, text="Rectangle", bg="#cfe3f7", font=("Helvetica", 16), command=self.go_to_rectangle_page)
        self.rectangle_button.pack(pady=10)

        self.square_button = tk.Button(self, text="Square", bg="#cfe3f7", font=("Helvetica", 16), command=self.go_to_square_page)
        self.square_button.pack(pady=10)

        self.triangle_button = tk.Button(self, text="Triangle", bg="#cfe3f7", font=("Helvetica", 16), command=self.go_to_triangle_page)
        self.triangle_button.pack(pady=10)

    def go_to_rectangle_page(self):
        from area_calculator_rectangle import RectanglePage
        self.master.destroy()
        RectanglePage().mainloop()

    def go_to_square_page(self):
        from area_calculator_square import SquarePage
        self.master.destroy()
        SquarePage().mainloop()

    def go_to_triangle_page(self):
        from area_calculator_triangle import TrianglePage
        self.master.destroy()
        TrianglePage().mainloop()