import tkinter as tk
import customtkinter as ctk
import HomePage
import time 
import random 

#set the basic GUI
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
        self.title_label = tk.Label(self.main_frame, text="Quiz!", font=("Helvetica", 50, "bold"), fg="#D2691E", bg="#FFE2CF")
        self.title_label.pack(pady=(20, 10))

        # Initialize quiz score and question number
        self.quiz_score = 0
        self.question_number = 0
        self.start_time = time.time()  # Record the start time

        # List of questions, each with text, options, and the correct answer index
        self.questions = [
            {"text": "What is the area of a square with a side length of 5?", "options": ["25", "13", "14", "15"], "answer_index": 0},
            {"text": "A square has a side length of 8. What is its area?", "options": ["13", "64", "4", "54"], "answer_index": 1},
            {"text": "Calculate the area of a square with a side length of 10.", "options": ["100", "13", "14", "15"], "answer_index": 0},
            {"text": "If a square has a side length of 12, what is its area?", "options": ["123", "40", "20", "144"], "answer_index": 3},
            {"text": "A rectangle has a length of 7 and a width of 3. What is its area?", "options": ["12", "21", "14", "15"], "answer_index": 1},
            {"text": "What is the area of a rectangle with a length of 15 and a width of 4?", "options": ["60", "94", "14", "0"], "answer_index": 0},
            {"text": "Find the area of a rectangle with a length of 9 and a width of 6.", "options": ["49", "56", "54", "35"], "answer_index": 2},
            {"text": "A rectangle has a length of 20 and a width of 5. What is its area?", "options": ["49", "56", "100", "35"], "answer_index": 2},
            {"text": "A triangle has a base of 10 and a height of 5. What is its area?", "options": ["49", "56", "25", "105"], "answer_index": 2},
            {"text": "What is the area of a triangle with a base of 8 and a height of 4?", "options": ["16", "56", "8", "875"], "answer_index": 0},
            {"text": "Calculate the area of a triangle with a base of 12 and a height of 7.", "options": ["49", "42", "98", "455"], "answer_index": 1},
            {"text": "If a triangle has a base of 14 and a height of 6, what is its area?", "options": ["49", "56", "68", "42"], "answer_index": 3},
            {"text": "A square has a side length of 11. What is its area?", "options": ["121", "11", "22", "111"], "answer_index": 0},
            {"text": "Calculate the area of a square with a side length of 6.", "options": ["36", "18", "24", "12"], "answer_index": 0},
            {"text": "If a square has a side length of 9, what is its area?", "options": ["18", "90", "81", "63"], "answer_index": 2},
            {"text": "What is the area of a square with a side length of 14?", "options": ["196", "28", "112", "140"], "answer_index": 0},
            {"text": "Find the area of a rectangle with a length of 12 and a width of 7.", "options": ["84", "21", "60", "49"], "answer_index": 0},
            {"text": "A rectangle has a length of 10 and a width of 8. What is its area?", "options": ["65.5", "18", "80", "72"], "answer_index": 2},
            {"text": "What is the area of a rectangle with a length of 5 and a width of 9?", "options": ["45", "14", "40", "35"], "answer_index": 0},
            {"text": "Calculate the area of a rectangle with a length of 16 and a width of 3.", "options": ["48", "30", "18", "60"], "answer_index": 0},
            {"text": "A rectangle has a length of 14 and a width of 4. What is its area?", "options": ["65", "36", "56", "64"], "answer_index": 2},
            {"text": "What is the area of a triangle with a base of 15 and a height of 6?", "options": ["45", "30", "90", "75"], "answer_index": 0},
            {"text": "Calculate the area of a triangle with a base of 9 and a height of 4.", "options": ["18", "36", "45", "27"], "answer_index": 0},
            {"text": "A triangle has a base of 11 and a height of 8. What is its area?", "options": ["88", "44", "98", "56"], "answer_index": 1},
            {"text": "If a triangle has a base of 7 and a height of 3, what is its area?", "options": ["10.5", "21", "14", "24.5"], "answer_index": 0},
            {"text": "What is the area of a triangle with a base of 13 and a height of 5?", "options": ["32.5", "25", "37.5", "30"], "answer_index": 2},
            {"text": "A rectangle has a length of 18 and a width of 5. What is its area?", "options": ["90", "72", "45", "82"], "answer_index": 0},
            {"text": "Calculate the area of a square with a side length of 3.", "options": ["9", "6", "12", "15"], "answer_index": 0},
            {"text": "What is the area of a triangle with a base of 20 and a height of 10?", "options": ["10", "200", "50", "100"], "answer_index": 3},
            {"text": "A rectangle has a length of 8 and a width of 11. What is its area?", "options": ["19", "18", "88", "66"], "answer_index": 2},
            {"text": "If a square has a side length of 17, what is its area?", "options": ["298", "170", "289", "34"], "answer_index": 2},
            {"text": "A square has a side length of 15. What is its area?", "options": ["225", "30", "45", "115"], "answer_index": 0},
            {"text": "Find the area of a rectangle with a length of 13 and a width of 6.", "options": ["78", "60", "72", "65"], "answer_index": 0},
            {"text": "A rectangle has a length of 11 and a width of 9. What is its area?", "options": ["99", "90", "88", "79"], "answer_index": 0},
            {"text": "Calculate the area of a square with a side length of 4.", "options": ["16", "8", "12", "10"], "answer_index": 0},
            {"text": "If a square has a side length of 18, what is its area?", "options": ["324", "36", "180", "162"], "answer_index": 0},
            {"text": "What is the area of a triangle with a base of 6 and a height of 3?", "options": ["18", "9", "12", "6"], "answer_index": 1},
            {"text": "A triangle has a base of 5 and a height of 7. What is its area?", "options": ["17.5", "12", "35", "10.5"], "answer_index": 0},
            {"text": "Calculate the area of a rectangle with a length of 7 and a width of 4.", "options": ["14", "21", "24", "28"], "answer_index": 3},
            {"text": "If a triangle has a base of 8 and a height of 6, what is its area?", "options": ["24", "14", "16", "48"], "answer_index": 0},
            {"text": "What is the area of a square with a side length of 7?", "options": ["49", "14", "21", "28"], "answer_index": 0},
            {"text": "A rectangle has a length of 6 and a width of 9. What is its area?", "options": ["54", "36", "45", "63"], "answer_index": 0},
            {"text": "Find the area of a triangle with a base of 4 and a height of 3.", "options": ["5.5", "6", "4.5", "12"], "answer_index": 1}
        ]   

 # Randomly select 10 questions from the list
        self.questions = random.sample(self.questions, 10)
        
        self.user_answers = []
        # Display the first question
        self.display_question()

    def display_question(self):
        # Check if there are more questions to display
        if self.question_number < len(self.questions):
            question = self.questions[self.question_number]
            
            # Clear the current window content
            self.clear_window()

            # Display the question text
            question_label = tk.Label(self.main_frame, text=f"{self.question_number + 1}. {question['text']}", wraplength=450, bg="#FFE2CF",fg="#D2691E", font=("Arial", 16, "bold"), padx=20, pady=20)
            question_label.pack(pady=20)
            
            # Display options as radio buttons
            self.option_var = tk.IntVar(value=-1)  # Set default value to -1 to ensure no pre-selection
            options_frame = tk.Frame(self.main_frame, bg="#FFE2CF")
            options_frame.pack(pady=20)

            for index, option in enumerate(question["options"]):
                option_button = tk.Radiobutton(options_frame, text=option, variable=self.option_var, value=index, bg="#FFA500", fg="#7E3501", font=("Helvetica", 16), anchor='w', width=20, indicatoron=0, padx=10, pady=10, selectcolor="#F67000")
                option_button.pack(anchor='center', pady=5)

            self.error_label = tk.Label(self.main_frame, text="", fg="#D2691E", bg="#FFE2CF", font=("Helvetica", 12))
            self.error_label.pack(pady=5)

            submit_button = ctk.CTkButton(self.main_frame, text="Submit", command=self.check_answer, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=100, height=25)
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
            feedback_label = tk.Label(self.main_frame, text=feedback, wraplength=450, bg="#FFE2CF", font=("Helvetica", 16, "bold"), fg="#D2691E")
            feedback_label.pack(pady=20)

            # Destroy the submit button
            for widget in self.main_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget('text') == 'Submit':
                    widget.destroy()

            # Display the "Next Question" button or "View Your Results" button
            if self.question_number < len(self.questions) - 1:
                next_button = ctk.CTkButton(self.main_frame, text="Next Question", command=self.next_question, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=100, height=25)
            else:
                next_button = ctk.CTkButton(self.main_frame, text="View Your Results", command=self.show_results, font=("Helvetica", 24), fg_color="#FFA500", text_color="black", hover_color="#FFB347", width=150, height=35)
            next_button.pack(pady=20)

# Function to move to the next question
    def next_question(self):
        self.question_number += 1
        self.display_question()

    def show_results(self):
         # Record the end time and calculate the total time taken
        end_time = time.time()
        total_time = end_time - self.start_time
        minutes, seconds = divmod(total_time, 60)
        # Clear the current window content
        self.clear_window()

        # Display the quiz results
        results_label = tk.Label(self.main_frame, text="Well Done!", bg="#FFE2CF", font=("Helvetica", 50, "bold"), fg="#D2691E")
        results_label.pack(pady=(20, 10))

        score_label = tk.Label(self.main_frame, text=f"Your Score Is {self.quiz_score}/{len(self.questions)} !", bg="#FFE2CF", font=("Helvetica", 24), fg="#D2691E")
        score_label.pack(pady=10)

        time_label = tk.Label(self.main_frame, text=f"Time Taken: {int(minutes)} minutes and {int(seconds)} seconds", bg="#FFE2CF", font=("Helvetica", 18), fg="#D2691E")
        time_label.pack(pady=10)


        # Add buttons to restart quiz, go to home page, and quit
        button_frame = tk.Frame(self.main_frame, bg="#FFE2CF")
        button_frame.pack(pady=20)

        restart_button = ctk.CTkButton(button_frame, text="Restart Quiz", command=self.restart_quiz, font=("Helvetica", 24), fg_color="#D2691E", text_color="black", hover_color="#FFB347", width=200, height=50)
        restart_button.pack(pady=10)

        home_button = ctk.CTkButton(button_frame, text="Home Page", command=self.navigate_to_homepage, font=("Helvetica", 24), fg_color="#D2691E", text_color="black", hover_color="#FFB347", width=200, height=50)
        home_button.pack(pady=10)

        quit_button = ctk.CTkButton(button_frame, text="Quit", command=self.root.quit, font=("Helvetica", 24), fg_color="#D2691E", text_color="black", hover_color="#FFB347", width=200, height=50)
        quit_button.pack(pady=10)

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
