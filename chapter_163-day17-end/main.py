# main.py

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank from the fetched data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize QuizBrain with the question bank
quiz = QuizBrain(question_bank)

# Run the quiz
while quiz.still_has_questions():
    quiz.next_question()

# Print the final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
