import random

# List of predefined words
word_list = ['ardvark', 'baboon', 'camel']

# Function to choose a random word
def choose_word(word_list):
    return random.choice(word_list)

# Function to prompt user for a letter guess
def guess_letter():
    return input("Guess a letter: ")

# Function to check if the guessed letter matches any letters in the chosen word
def check_guess(word, letter):
    positions = [i for i, char in enumerate(word) if char == letter]
    return positions

# Main program
def main():
    # Choose a random word
    chosen_word = choose_word(word_list)
    print("Chosen word:", chosen_word)

    # Prompt user for a letter guess
    guessed_letter = guess_letter()

    # Check if the guessed letter matches any letters in the chosen word
    matching_positions = check_guess(chosen_word, guessed_letter)

    # Display positions where the guessed letter matches in the chosen word
    print("The guessed letter '{}' matches at positions: {}".format(guessed_letter, matching_positions))

# Run the program
if __name__ == "__main__":
    main()
