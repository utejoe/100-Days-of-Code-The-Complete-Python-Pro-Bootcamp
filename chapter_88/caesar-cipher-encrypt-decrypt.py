def caesar(start_text, shift_amount, cipher_direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    end_text = ""
    
    # Adjust shift_amount for decoding
    if cipher_direction == 'decode':
        shift_amount *= -1
    
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += letter
    
    print(f"The {cipher_direction}d text is {end_text}")

# Get user inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Call the caesar function with appropriate arguments
caesar(text, shift, direction)
