def caesar_cipher(text, shift, direction):
    result = ""  # Initialize an empty string to store the encrypted or decrypted text
    if direction == "decode":  # Check if the direction is to decode
        shift = -shift  # Reverse the shift to decode the text

    for char in text:  # Iterate through each character in the text
        if char.isalpha():  # Check if the character is a letter
            shift_amount = ord('A') if char.isupper() else ord('a')  # Set the shift amount based on the character's case
            shifted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)  # Apply the Caesar cipher algorithm
            result += shifted_char  # Add the shifted character to the result
        else:
            result += char  # If the character is not a letter, add it to the result unchanged
    return result  # Return the encrypted or decrypted text


def main():
    while True:  # Start an indefinite loop for user interaction
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()  # Prompt the user for encryption or decryption
        text = input("Type your message:\n").lower()  # Prompt the user to enter the text to be encrypted or decrypted
        shift = int(input("Type the shift number:\n"))  # Prompt the user for the shift value

        if direction in ["encode", "decode"]:  # Check if the user input is valid
            print(f"The {direction}d text is: {caesar_cipher(text, shift, direction)}")  # Print the encrypted or decrypted text
        
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()  # Ask the user if they want to continue
        if restart != 'yes':  # If the user does not want to continue
            break  # Exit the loop and end the program


if __name__ == "__main__":
    main()  # Call the main function if the script is run as the main program
