import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

# User inputs
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# Easy level password generation
password = ""

# Generate letters
for _ in range(num_letters):
    password += random.choice(letters)

# Generate symbols
for _ in range(num_symbols):
    password += random.choice(symbols)

# Generate numbers
for _ in range(num_numbers):
    password += random.choice(numbers)

# Shuffle the password
password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)

print(f"Your password is: {shuffled_password}")