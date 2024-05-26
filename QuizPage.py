import tkinter as tk
import HomePage

class Page3:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Quiz!")
        self.root.geometry("500x700")
        self.root.configure(bg="#FFE2CF")
        self.root.resizable(False, False)

        # Create a border frame
        border_frame = tk.Frame(self.root, bg="#FFA500", bd=10)
        border_frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=680)
        
        # Create an inner frame
        self.main_frame = tk.Frame(border_frame, bg="#FFE2CF")
        self.main_frame.pack(fill="both", expand=True)
        
        # Create the title label
        self.title_label = tk.Label(self.main_frame, text="Quiz", font=("Helvetica", 50, "bold"), fg="#D2691E", bg="#FFE2CF")
        self.title_label.pack(pady=(20, 10))

        # Initialize quiz score and question number
        self.quiz_score = 0
        self.question_number = 0

        # List of questions, each with text, options, and the correct answer index
        self.questions = [
            {"text": "What is the area of a rectangle with a length of 3 and a width of 4?", "options": ["12", "13", "14", "15"], "answer_index": 0},
            {"text": "What is the area of a triangle with a length of 5 and a width of 9?", "options": ["13", "27", "4", "54"], "answer_index": 1},
            {"text": "What is the area of a rectangle with a length of 6 and a width of 2?", "options": ["12", "13", "14", "15"], "answer_index": 0},
            {"text": "What is the area of a square with a length of 20?", "options": ["123", "40", "20", "400"], "answer_index": 3},
            {"text": "What is the area of a triangle with a length of 10 and a width of 10?", "options": ["12", "50", "14", "15"], "answer_index": 1},
            {"text": "What is the area of a square with a length of 7?", "options": ["49", "94", "14", "0"], "answer_index": 0},
            {"text": "Challenge Question: What is the area of a rectangle with a length of 7 and a width of 7?", "options": ["49", "56", "42", "35"], "answer_index": 0}
        ]
        
        # Display the first question
        self.display_question()

    def display_question(self):
        # Check if there are more questions to display
        if self.question_number < len(self.questions):
            question = self.questions[self.question_number]
            
            # Clear the current window content
            self.clear_window()

            # Display the question text
            question_label = tk.Label(self.main_frame, text=f"{self.question_number + 1}. {question['text']}", wraplength=450, bg="#FFE2CF", font=("Arial", 16, "bold"), padx=20, pady=20)
            question_label.pack(pady=20)
            
            # Display options as radio buttons
            self.option_var = tk.IntVar(value=-1)  # Set default value to -1 to ensure no pre-selection
            options_frame = tk.Frame(self.main_frame, bg="#FFE2CF")
            options_frame.pack(pady=20)

            for index, option in enumerate(question["options"]):
                option_button = tk.Radiobutton(options_frame, text=option, variable=self.option_var, value=index, bg="#FFE2CF", fg="#8B4513", font=("Helvetica", 16), anchor='w', width=20, indicatoron=0, padx=10, pady=10, selectcolor="#F67000")
                option_button.pack(anchor='center', pady=5)

            self.error_label = tk.Label(self.main_frame, text="", fg="red", bg="#FFE2CF", font=("Helvetica", 12))
            self.error_label.pack(pady=5)

            submit_button = tk.Button(self.main_frame, text="Submit", command=self.check_answer, bg="#FF9A76", font=("Helvetica", 14, "bold"))
            submit_button.pack(pady=20)
        else:
            # If all questions have been answered, show the results
            self.show_results()

    def clear_window(self):
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def check_answer(self):
        if self.option_var.get() == -1:
            self.error_label.config(text="Please select an option")
        else:
            question = self.questions[self.question_number]
            # Retrieve the user's answer
            user_selection = self.option_var.get()  # Get the index of the selected option

            # Check if the user's answer is correct
            correct_answer_index = question["answer_index"]
            if user_selection == correct_answer_index:
                feedback = "You are correct!"
                self.quiz_score += 1
            else:
                feedback = f"You are incorrect, the correct answer is {question['options'][correct_answer_index]}"
            
            # Display feedback message
            feedback_label = tk.Label(self.main_frame, text=feedback, wraplength=450, bg="#FFE2CF", font=("Helvetica", 16, "bold"))
            feedback_label.pack(pady=20)

            # Destroy the submit button
            for widget in self.main_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget('text') == 'Submit':
                    widget.destroy()

            # Display the "Next Question" button or "View Your Results" button
            if self.question_number < len(self.questions) - 1:
                next_button = tk.Button(self.main_frame, text="Next Question", command=self.next_question, bg="#FF9A76", font=("Helvetica", 14, "bold"))
            else:
                next_button = tk.Button(self.main_frame, text="View Your Results", command=self.show_results, bg="#FF9A76", font=("Helvetica", 14, "bold"))
            next_button.pack(pady=20)

    def next_question(self):
        # Move to the next question
        self.question_number += 1
        self.display_question()

    def show_results(self):
        # Clear the current window content
        self.clear_window()

        # Display the quiz results
        results_label = tk.Label(self.main_frame, text="Well Done!", bg="#FFE2CF", font=("Helvetica", 50, "bold"), fg="#D2691E")
        results_label.pack(pady=(20, 10))

        score_label = tk.Label(self.main_frame, text=f"Your Score Is {self.quiz_score}/{len(self.questions)} !", bg="#FFE2CF", font=("Helvetica", 24))
        score_label.pack(pady=10)

        # Add buttons to restart quiz, go to home page, and quit
        button_frame = tk.Frame(self.main_frame, bg="#FFE2CF")
        button_frame.pack(pady=20)

        restart_button = tk.Button(button_frame, text="Restart Quiz", command=self.restart_quiz, bg="#FFA500", font=("Helvetica", 14), width=15)
        restart_button.grid(row=0, column=0, padx=10, pady=10)

        home_button = tk.Button(button_frame, text="Home Page", command=self.navigate_to_homepage, bg="#FFA500", font=("Helvetica", 14), width=15)
        home_button.grid(row=0, column=1, padx=10, pady=10)

        quit_button = tk.Button(button_frame, text="Quit", command=self.root.quit, bg="#FFA500", font=("Helvetica", 14), width=15)
        quit_button.grid(row=0, column=2, padx=10, pady=10)

        # Add shapes at the bottom (images replaced with labels for simplicity)
        shapes_frame = tk.Frame(self.main_frame, bg="#FFE2CF")
        shapes_frame.pack(pady=20)

        shapes = ["Circle", "Triangle", "Square", "Pentagon"]
        colors = ["#FFA500", "#32CD32", "#1E90FF", "#FF69B4"]
        for shape, color in zip(shapes, colors):
            shape_label = tk.Label(shapes_frame, text=shape, bg=color, fg="white", font=("Helvetica", 14), width=10, height=3)
            shape_label.pack(side="left", padx=10)

    def restart_quiz(self):
        # Reset the quiz score and question number
        self.quiz_score = 0
        self.question_number = 0
        self.display_question()
        
    def navigate_to_homepage(self):
        # Close the current Page3 and navigate to Home Page
        self.clear_window()
        HomePage.Page1(self.root)

if __name__ == "__main__":
    # Initialize the Tkinter root window
    root = tk.Tk()
    app = Page3(root)
    root.mainloop()
