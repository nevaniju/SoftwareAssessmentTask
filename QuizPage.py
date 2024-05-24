import tkinter as tk

class Page3:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Quiz!")
        self.root.geometry("500x700")
        self.root.configure(bg="#FFA500")

        self.border_frame = tk.Frame(self.root, bg="#FFE2CF", bd=10)
        self.border_frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=680)
        
        # Initialize quiz score and question number
        self.quiz_score = 0
        self.question_number = 0

        # List of questions, each with text, options, and the correct answer index
        self.questions = [
            {"text": "Question 1: What is the area of a rectangle with a length of 3 and a width of 4?",
             "options": ["12", "13", "14", "15"], "answer_index": 0},
            {"text": "Question 2: What is the area of a triangle with a length of 6 and a width of 9?",
             "options": ["45", "54", "27", "72"], "answer_index": 2},
            {"text": "Question 3: What is the area of a rectangle with a length of 6 and a width of 2?",
             "options": ["12", "13", "14", "15"], "answer_index": 0},
            {"text": "Question 4: What is the area of a square with a length of 20?",
             "options": ["123", "40", "20", "400"], "answer_index": 3},
            {"text": "Question 5: What is the area of a triangle with a length of 10 and a width of 10?",
             "options": ["12", "50", "14", "15"], "answer_index": 1},
            {"text": "Question 6: What is the area of a square with a length of 7?",
             "options": ["49", "94", "14", "0"], "answer_index": 0},
            {"text": "Question 7: Challenge Question 10: What is the area of the following shape?",
             "options": None, "answer_index": None}  # User will input the answer directly
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
            question_label = tk.Label(self.root, text=question["text"], wraplength=450, bg="#FFE2CF", font=("Helvetica", 16, "bold"))
            question_label.pack(pady=20)
            
            # Display options as radio buttons (if applicable)
            if question["options"]:
                self.option_var = tk.IntVar()  # Change StringVar to IntVar to store the index
                options_frame = tk.Frame(self.root, bg="#FFE2CF")
                options_frame.pack(pady=20)

                # Use enumerate to get both index and option
                for index, option in enumerate(question["options"]):
                    option_button = tk.Radiobutton(options_frame, text=option, variable=self.option_var, value=index, 
                                                   bg="#FFE2CF", font=("Helvetica", 14), anchor='w', width=20, 
                                                   indicatoron=0, padx=10, pady=10, selectcolor="#FFD7AF")
                    option_button.pack(anchor='center', pady=5)

                submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, bg="#FF9A76", font=("Helvetica", 14, "bold"))
                submit_button.pack(pady=20)
            else:
                # For questions without options, provide an entry field for user input
                self.answer_entry = tk.Entry(self.root, font=("Helvetica", 14))
                self.answer_entry.pack(pady=20)
                submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, bg="#FF9A76", font=("Helvetica", 14, "bold"))
                submit_button.pack(pady=20)
        else:
            # If all questions have been answered, show the results
            self.show_results()

    def clear_window(self):
        # Clear all widgets from the window
        for widget in self.root.winfo_children():
            widget.destroy()

    def check_answer(self):
        question = self.questions[self.question_number]
        
        # Retrieve the user's answer
        if question["options"]:
            user_selection = self.option_var.get()  # Get the index of the selected option
        else:
            user_selection = self.answer_entry.get()

        # Check if the user's answer is correct
        if question["options"]:
            correct_answer_index = question["answer_index"]
            if user_selection == correct_answer_index:
                feedback = "You are correct!"
                self.quiz_score += 1
            else:
                feedback = f"You are incorrect, the correct answer is {question['options'][correct_answer_index]}"
        else:
            if user_selection == str(question["answer_index"]):  # Convert to string for direct comparison
                feedback = "You are correct!"
                self.quiz_score += 1
            else:
                feedback = f"You are incorrect, the correct answer is {question['answer_index']}"
    
        # Clear window and display feedback
        self.clear_window()
        feedback_label = tk.Label(self.root, text=feedback, wraplength=450, bg="#FFE2CF", font=("Helvetica", 16, "bold"))
        feedback_label.pack(pady=20)
        next_button = tk.Button(self.root, text="Next Question", command=self.next_question, bg="#FF9A76", font=("Helvetica", 14, "bold"))
        next_button.pack(pady=20)

    def next_question(self):
        # Move to the next question
        self.question_number += 1
        self.display_question()

    def show_results(self):
        # Clear the window and display the final score
        self.clear_window()
        result_label = tk.Label(self.root, text=f"Your final score is: {self.quiz_score} out of {len(self.questions)}", bg="#FFE2CF", font=("Helvetica", 16, "bold"))
        result_label.pack(pady=20)
        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="#FF9A76", font=("Helvetica", 14, "bold"))
        exit_button.pack(pady=20)

if __name__ == "__main__":
    # Initialize the Tkinter root window
    root = tk.Tk()
    
    # Create an instance of the QuizApp
    app = Page3(root)
    
    # Run the Tkinter main loop
    root.mainloop()
