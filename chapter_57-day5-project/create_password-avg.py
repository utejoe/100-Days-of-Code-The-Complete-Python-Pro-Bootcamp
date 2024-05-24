import random

# Lists of letters, symbols, and numbers
letters = ['a', 'b', 'c', ..., 'Z']
symbols = ['!', '@', '#', ..., '&']
numbers = ['0', '1', '2', ..., '9']

# User input for the desired number of characters
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# Easy Level: Generate password in sequence
password_easy = ""
for _ in range(num_letters):
    password_easy += random.choice(letters)
for _ in range(num_symbols):
    password_easy += random.choice(symbols)
for _ in range(num_numbers):
    password_easy += random.choice(numbers)
print("Easy Level Password:", password_easy)

# Hard Level: Generate password with characters in random order
password_hard = []
for _ in range(num_letters):
    password_hard.append(random.choice(letters))
for _ in range(num_symbols):
    password_hard.append(random.choice(symbols))
for _ in range(num_numbers):
    password_hard.append(random.choice(numbers))
random.shuffle(password_hard)
password_hard = ''.join(password_hard)
print("Hard Level Password:", password_hard)
