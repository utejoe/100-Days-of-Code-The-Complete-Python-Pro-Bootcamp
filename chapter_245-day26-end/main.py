import pandas as pd

# Step 1: Creating a Dictionary from the NATO Phonetic Alphabet CSV

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary using dictionary comprehension
phonetic_dictionary = {row['Letter']: row['Code'] for index, row in data.iterrows()}

# Step 2: Creating a List of Phonetic Code Words for User Input

def phonetic_code(word):
    word = word.upper()  # Convert word to uppercase to match keys in phonetic_dictionary
    code_words = [phonetic_dictionary[letter] for letter in word if letter in phonetic_dictionary]
    return code_words

# Example usage:
if __name__ == '__main__':
    user_input = input("Enter a word: ")
    result = phonetic_code(user_input)
    print(result)
