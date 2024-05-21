import tkinter as tk

class QuizPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#faf0be")
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Quiz", font=("Helvetica", 24, "bold"), bg="#faf0be", pady=20)
        self.title_label.pack()

        # Add widgets for the Quiz page here

if __name__ == "__main__":
    root = tk.Tk()
    QuizPage(root).pack(side="top", fill="both", expand=True)
    root.mainloop()