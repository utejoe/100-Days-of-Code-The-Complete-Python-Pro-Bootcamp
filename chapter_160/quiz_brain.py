class QuizBrain:
    # Initialize the QuizBrain class with a question list
    def __init__(self, q_list):
        self.question_number = 0  # Start from the first question
        self.question_list = q_list  # List of questions
        self.score = 0  # Initialize score to 0

    # Method to display the next question
    def next_question(self):
        current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Increment the question number
        # Prompt the user for their answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    # Method to check the user's answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():  # Case-insensitive comparison 
            self.score += 1  # Increment the score if the answer is correct
            print("You got it right!")
        else:
            print("That's wrong.")
        # Provide feedback on the correct answer and the user's current score
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

# Assuming you have a list of question objects with 'text' and 'answer' attributes
# Example:
# question_list = [
#     Question(text="The sky is blue.", answer="True"),
#     Question(text="The grass is red.", answer="False"),
#     # Add more questions here
# ]

# Create an instance of the QuizBrain class
# quiz = QuizBrain(question_list)

# To start the quiz, you would typically loop through the questions:
# while quiz.still_has_questions():
#     quiz.next_question()
