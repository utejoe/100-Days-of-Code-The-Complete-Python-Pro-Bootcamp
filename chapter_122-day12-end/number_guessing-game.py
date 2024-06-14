import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

ART = """
  ____                       _   _                 _                 
 / ___|_ __ ___  __ _ _   _| | | | __ _ _ __ __ _| |__   __ _ _ __  
| |  _| '__/ _ \/ _` | | | | |_| |/ _` | '__/ _` | '_ \ / _` | '_ \ 
| |_| | | |  __/ (_| | |_| |  _  | (_| | | | (_| | | | | (_| | | | |
 \____|_|  \___|\__, |\__,_|_| |_|\__,_|_|  \__, |_| |_|\__,_|_| |_|
                |___/                      |___/                   
"""

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True

def game():
    print(ART)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)
    # print(f"Pssst, the correct answer is {answer}")  # Debugging line, you can comment it out later
    
    turns = set_difficulty()
    guess = None
    
    while turns > 0 and guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if check_answer(guess, answer):
            break
        
        turns -= 1
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")

# Run the game
game()
