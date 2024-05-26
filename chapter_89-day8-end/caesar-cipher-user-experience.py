# Main script
from art import logo  # Importing the logo from the art module

# Caesar cipher function
def caesar(start_text, shift_amount, cipher_direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    end_text = ""

    # Adjust shift_amount for decoding
    if cipher_direction == 'decode':
        shift_amount *= -1  # Reverse the shift for decoding
    
    # Ensure the shift_amount is within the range of 0-25
    shift_amount = shift_amount % 26

    # Iterate through each character in the start_text
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            end_text += new_letter  # Add the new letter to the end_text
        else:
            end_text += char  # If the character is not in the alphabet, keep it unchanged
    
    # Print the encrypted or decrypted text
    print(f"The {cipher_direction}d text is {end_text}")

# Print the logo
print(logo)

should_continue = True

# Loop to allow for multiple encryptions or decryptions
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function with the provided inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # Prompt the user to continue or end
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False  # Exit the loop if the user chooses not to continue
        print("Goodbye")  # Print a farewell message
