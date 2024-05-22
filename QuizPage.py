import tkinter as tk

class Page3:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Area!")
        self.root.geometry("500x700")
        self.root.configure(bg="#FFE2CF")
        
        # Initialize quiz score and question number
        self.quiz_score = 0
        self.question_number = 0
        
        # List of questions, each with text, options, and the correct answer
        self.questions = [
            {"text": "Question 1: What is the area of a rectangle with a length of 3 and a width of 4?",
             "options": ["12", "13", "14", "15"], "answer": "12"},
            {"text": "Question 2: What is the area of a triangle with a length of 6 and a width of 9?",
             "options": ["45", "54", "27", "72"], "answer": "27"},
            {"text": "Question 3: What is the area of a rectangle with a length of 6 and a width of 2?",
             "options": ["12", "13", "14", "15"], "answer": "12"},
            {"text": "Question 4: What is the area of a square with a length of 20?",
             "options": ["123", "40", "20", "400"], "answer": "400"},
            {"text": "Question 5: What is the area of a triangle with a length of 10 and a width of 10?",
             "options": ["12", "50", "14", "15"], "answer": "50"},
            {"text": "Question 6: What is the area of a square with a length of 7?",
             "options": ["49", "94", "14", "0"], "answer": "49"},
            {"text": "Question 7: Challenge Question 10: What is the area of the following shape?",
             "options": None, "answer": "605"}  # User will input the answer directly
        ]
        
        # Display the first question
        self.display_question()

   

if __name__ == "__main__":
    # Initialize the Tkinter root window
    root = tk.Tk()
    
    # Create an instance of the QuizApp
    app = Page3(root)
    
    # Run the Tkinter main loop
    root.mainloop()
