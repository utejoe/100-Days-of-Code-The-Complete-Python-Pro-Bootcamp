# data.py

import requests

def get_question_data():
    # URL for fetching questions from Open Trivia Database
    url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"
    
    response = requests.get(url)
    question_data = response.json()["results"]
    return question_data

# Fetch the questions when this module is imported
question_data = get_question_data()
