# Initialize a variable to track whether the game is over
end_of_game = False

# Start the repeatability loop
while not end_of_game:
    # Generate a list of blanks representing the letters in the chosen word
    display = ['_' for _ in range(len(chosen_word))]
    
    # Loop to allow the user to guess letters until the word is complete
    while '_' in display:
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
            print("Wrong guess! Try again.")
    
    # Check if all blanks in the display are filled
    if '_' not in display:
        print("Congratulations! You've won!")
    
    # End the game
    end_of_game = True
