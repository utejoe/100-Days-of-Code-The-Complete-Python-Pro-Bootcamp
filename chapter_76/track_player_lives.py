# Initialize the variable to track the number of lives
lives = 6

# Define ASCII art representing the stages of the hangman game
stages = [
    """
     --------
     |      |
     |      O
     |     \\|/
     |      |
     |     / \\
    ---
    """,
    """
     --------
     |      |
     |      O
     |     \\|/
     |      |
     |     /
    ---
    """,
    """
     --------
     |      |
     |      O
     |     \\|/
     |      |
     |
    ---
    """,
    """
     --------
     |      |
     |      O
     |     \\|
     |      |
     |
    ---
    """,
    """
     --------
     |      |
     |      O
     |      |
     |      |
     |
    ---
    """,
    """
     --------
     |      |
     |      O
     |    
     |     
     |
    ---
    """,
    """
     --------
     |      |
     |      
     |    
     |     
     |
    ---
    """
]

# Repeatability loop
while lives > 0:
    # Generate a list of blanks representing the letters in the chosen word
    display = ['_' for _ in range(len(chosen_word))]

    # Prompt the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Replace blanks with correct letters if guessed right
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Correct guess! Current word:", ''.join(display))
    else:
        # Decrement lives on incorrect guess
        lives -= 1
        print("Wrong guess! You have", lives, "lives remaining.")
    
    # Print the corresponding hangman stage
    print(stages[lives])

# Check if the user has run out of lives
if lives == 0:
    print("You lose.")
