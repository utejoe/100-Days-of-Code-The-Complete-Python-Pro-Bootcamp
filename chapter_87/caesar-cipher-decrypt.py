def encrypt(plain_text, shift_amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""
    
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plain_text = ""
    
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter
    
    print(f"The decoded text is {plain_text}")

# Get user inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Call the appropriate function based on the user's choice
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
