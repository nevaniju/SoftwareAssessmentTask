import tkinter as tk
import PIL
from PIL import Image, ImageTk

class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LearnPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

class LearnPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.master.geometry("400x600")  # Set the window size to 400x600
        label = tk.Label(self, text="This is the Learn page")
        label.pack()
        button = tk.Button(self, text="Go to Quiz page", command=lambda: app.switch_frame(QuizPage))
        button.pack()

        # Load an image using PIL
        image = Image.open("/Users/nevaaa/Desktop/Software Engineering/SoftwareAssessmentTask/trianglefacee.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo)
        image_label.image = photo  # Keep a reference to prevent garbage collection
        image_label.pack()

class QuizPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the Quiz page")
        label.pack()
        button = tk.Button(self, text="Go to Area Calculator page", command=lambda: app.switch_frame(AreaCalculatorPage))
        button.pack()

class AreaCalculatorPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.shape_var = tk.IntVar()
        self.shape_var.set(1)

        tk.Label(self, text="Select the shape:").pack()
        tk.Radiobutton(self, text="Rectangle", variable=self.shape_var, value=1).pack()
        tk.Radiobutton(self, text="Square", variable=self.shape_var, value=2).pack()
        tk.Radiobutton(self, text="Triangle", variable=self.shape_var, value=3).pack()

        self.side1_var = tk.StringVar()
        self.side2_var = tk.StringVar()
        self.side3_var = tk.StringVar()

        tk.Label(self, text="Side 1:").pack()
        tk.Entry(self, textvariable=self.side1_var).pack()
        tk.Label(self, text="Side 2:").pack()
        tk.Entry(self, textvariable=self.side2_var).pack()
        tk.Label(self, text="Side 3:").pack()
        tk.Entry(self, textvariable=self.side3_var).pack()

        tk.Button(self, text="Calculate Area", command=self.calculate_area).pack()

    def calculate_area(self):
        if self.shape_var.get() == 1:
            # Rectangle
            side1 = float(self.side1_var.get())
            side2 = float(self.side2_var.get())
            area = side1 * side2
        elif self.shape_var.get() == 2:
            # Square
            side = float(self.side1_var.get())
            area = side * side
        else:
            # Triangle
            side1 = float(self.side1_var.get())
            side2 = float(self.side2_var.get())
            area = (side1 + side2) / 2

        # Switch tothe results page
        ResultsPage(self.master, area=area)
        self.master.switch_frame(ResultsPage)

class ResultsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        area = kwargs.pop("area")
        tk.Label(self, text=f"The area is: {area}").pack()
        tk.Button(self, text="Back to Area Calculator", command=lambda: app.switch_frame(AreaCalculatorPage)).pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()