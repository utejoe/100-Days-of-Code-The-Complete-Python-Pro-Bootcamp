import requests
import html
from tkinter import *

# Define the number of questions and type of questions (boolean for true/false)
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Fetching the data from Open Trivia Database API
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# Function to format questions
def format_question(question):
    return html.unescape(question)

# Tkinter setup
window = Tk()
window.title("Quizzler")

score = 0
question_number = 0

question_text = StringVar()
score_text = StringVar()

# Displaying the question
def display_question():
    global question_number
    if question_number < len(question_data):
        q = format_question(question_data[question_number]['question'])
        question_text.set(q)
    else:
        question_text.set("Quiz Over! Your final score is: {}".format(score))

# Checking the answer
def check_answer(user_answer):
    global question_number, score
    correct_answer = question_data[question_number]['correct_answer']
    if user_answer == correct_answer:
        score += 1
    question_number += 1
    display_question()
    score_text.set("Score: {}".format(score))

# Setting up the UI
question_label = Label(window, textvariable=question_text, wraplength=300)
question_label.pack(pady=20)

true_button = Button(window, text="True", command=lambda: check_answer("True"))
true_button.pack(side="left", padx=20)

false_button = Button(window, text="False", command=lambda: check_answer("False"))
false_button.pack(side="right", padx=20)

score_label = Label(window, textvariable=score_text)
score_label.pack(pady=20)

# Initialize the quiz
score_text.set("Score: 0")
display_question()

window.mainloop()
