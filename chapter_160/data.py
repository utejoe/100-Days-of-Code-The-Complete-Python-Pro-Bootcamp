# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Chocolate affects a dog's heart and nervous system; a few ounces are enough to kill a small dog.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"}
# ]


import requests

# URL for fetching questions from Open Trivia Database
url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"

response = requests.get(url)
question_data = response.json()["results"]