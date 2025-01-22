import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        # List of questions and options
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "Who developed the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Jupiter", "Saturn", "Mars"],
                "answer": "Jupiter"
            }
        ]
        
        self.score = 0
        self.question_index = 0
        
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", font=("Arial", 12), width=20, command=lambda i=i: self.check_answer(i))
            button.grid(row=i, column=0, pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(pady=20)
    
    def show_question(self):
        question_data = self.questions[self.question_index]
        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)

    def check_answer(self, selected_option):
        question_data = self.questions[self.question_index]
        correct_answer = question_data["answer"]

        if self.option_buttons[selected_option].cget("text") == correct_answer:
            self.score += 1
        
        self.question_index += 1

        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.end_game()

        self.score_label.config(text=f"Score: {self.score}")

    def end_game(self):
        messagebox.showinfo("Quiz Finished", f"Game Over! Your final score is: {self.score}")
        self.root.quit()

# Create the Tkinter root window
root = tk.Tk()

# Create and start the quiz game
quiz_game = QuizGame(root)

# Start the Tkinter event loop
root.mainloop()
