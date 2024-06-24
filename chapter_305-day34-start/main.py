import tkinter as tk
from tkinter import messagebox
import requests
import html

class QuizzlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quizzler App")
        self.score = 0
        self.questions = []
        self.current_question_index = 0
        
        self.question_label = tk.Label(root, text="Loading question...", wraplength=300)
        self.question_label.pack(pady=20)
        
        self.true_button = tk.Button(root, text="True", command=self.answer_true)
        self.true_button.pack(pady=10)
        
        self.false_button = tk.Button(root, text="False", command=self.answer_false)
        self.false_button.pack(pady=10)
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.score_label.pack(pady=20)
        
        self.fetch_questions()
    
    def fetch_questions(self):
        # Fetch questions from the API
        self.questions = self.get_questions(amount=10, category=9, difficulty="medium", type="boolean")
        if self.questions:
            self.current_question_index = 0
            self.update_question()
        else:
            messagebox.showerror("Error", "Failed to fetch questions.")
    
    def get_questions(self, amount=10, category=9, difficulty="medium", type="boolean"):
        url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={type}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            print(f"Failed to fetch questions. Status code: {response.status_code}")
            return None
    
    def update_question(self):
        if self.current_question_index < len(self.questions):
            question_text = self.questions[self.current_question_index]["question"]
            self.question_label.config(text=question_text)
        else:
            messagebox.showinfo("Quiz Completed", f"You've completed the quiz!\nFinal Score: {self.score}")
    
    def answer_true(self):
        if self.current_question_index < len(self.questions):
            correct_answer = self.questions[self.current_question_index]["correct_answer"]
            if correct_answer.lower() == "true":
                self.score += 1
            self.current_question_index += 1
            self.update_question()
            self.update_score_label()
    
    def answer_false(self):
        if self.current_question_index < len(self.questions):
            correct_answer = self.questions[self.current_question_index]["correct_answer"]
            if correct_answer.lower() == "false":
                self.score += 1
            self.current_question_index += 1
            self.update_question()
            self.update_score_label()
    
    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizzlerApp(root)
    root.mainloop()
