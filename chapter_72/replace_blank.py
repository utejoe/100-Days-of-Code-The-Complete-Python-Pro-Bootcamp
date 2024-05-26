# Generate a list of blanks representing the letters in the chosen word
blanks = ['_' for _ in range(len(chosen_word))]

# Replace blanks with correct letters if guessed right
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        blanks[i] = guess

# Print the updated list with correct guesses
print(blanks)
