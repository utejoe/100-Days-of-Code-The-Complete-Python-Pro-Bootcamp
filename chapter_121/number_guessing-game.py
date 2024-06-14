import random
from art import logo

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    attempts = set_difficulty()
    guess = 0
    while guess != random_number and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {random_number}.")
    if attempts == 0 and guess != random_number:
        print("You've run out of guesses, you lose.")

while input("Do you want to play again? Type 'y' or 'n': ") == 'y':
    game()
