import pandas as pd

# Load the NATO phonetic alphabet CSV file into a DataFrame
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame
phonetic_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Function to generate phonetic list from user input
def generate_phonetic():
    # Prompt the user to enter a word
    word = input("Enter a word: ").upper()
    try:
        # Create a list of phonetic codes for the given word
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # Handle the case where the user input contains non-alphabetical characters
        print("Sorry, only letters in the alphabet please.")
        # Recursively call the function to prompt the user again
        generate_phonetic()
    else:
        # Print the resulting list of phonetic codes
        print(output_list)

# Call the function to start the program
generate_phonetic()
