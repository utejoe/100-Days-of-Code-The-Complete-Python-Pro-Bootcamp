def encrypt(plain_text, shift_amount):
    # Define the alphabet used for encryption
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""  # Initialize an empty string to store the encrypted text
    
    # Iterate through each letter in the plain text
    for letter in plain_text:
        # Check if the letter is in the alphabet
        if letter in alphabet:
            # Find the position of the letter in the alphabet
            position = alphabet.index(letter)
            # Calculate the new position after shifting
            new_position = (position + shift_amount) % 26
            # Find the new letter corresponding to the new position
            new_letter = alphabet[new_position]
            # Append the new letter to the encrypted text
            cipher_text += new_letter
        else:
            # If the character is not in the alphabet, keep it unchanged
            cipher_text += letter
    
    # Print the encrypted text
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    # Define the alphabet used for decryption
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plain_text = ""  # Initialize an empty string to store the decrypted text
    
    # Iterate through each letter in the cipher text
    for letter in cipher_text:
        # Check if the letter is in the alphabet
        if letter in alphabet:
            # Find the position of the letter in the alphabet
            position = alphabet.index(letter)
            # Calculate the new position after shifting
            new_position = (position - shift_amount) % 26
            # Find the new letter corresponding to the new position
            new_letter = alphabet[new_position]
            # Append the new letter to the decrypted text
            plain_text += new_letter
        else:
            # If the character is not in the alphabet, keep it unchanged
            plain_text += letter
    
    # Print the decrypted text
    print(f"The decoded text is {plain_text}")

# Get user inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Call the appropriate function based on the user's choice
if direction == 'encode':
    encrypt(text, shift)  # Encrypt the text with the specified shift
elif direction == 'decode':
    decrypt(text, shift)  # Decrypt the text with the specified shift
