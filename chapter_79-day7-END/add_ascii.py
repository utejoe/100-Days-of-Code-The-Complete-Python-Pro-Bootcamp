import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (here, os.name is 'posix')
    else:
        os.system('clear')

# Printing the hangman logo at the start of the game
print(logo)

# Select a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_' for _ in range(word_length)]
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()  # Clear the screen after each guess

    if guess in guessed_letters:
        print(f"You've already guessed {guess}.")
    else:
        guessed_letters.append(guess)
        
        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        print(f"{' '.join(display)}")
        
        if '_' not in display:
            end_of_game = True
            print("You win.")
        elif lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(stages[lives])
