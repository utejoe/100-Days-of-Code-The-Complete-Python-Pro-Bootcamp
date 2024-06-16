# Increment each number in the list by 1 using a loop
numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    new_numbers.append(n + 1)
print(new_numbers)  # Output: [2, 3, 4]

# Increment each number in the list by 1 using list comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)  # Output: [2, 3, 4]

# List comprehension with strings
# Splitting a string into a list of its characters
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)  # Output: ['A', 'n', 'g', 'e', 'l', 'a']

# List comprehension with a range
# Creating a list by doubling the numbers in a range
range_list = [num * 2 for num in range(1, 5)]
print(range_list)  # Output: [2, 4, 6, 8]

# Conditional list comprehension
# Filtering a list to include only items that meet a certain condition
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)  # Output: ['Alex', 'Beth', 'Dave']

# Conditional list comprehension with transformation
# Transforming names to uppercase if they have five or more letters
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)  # Output: ['CAROLINE', 'ELEANOR', 'FREDDIE']

# Challenges
# Create a list of squares of numbers from 1 to 10
squares = [num ** 2 for num in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a list of even numbers from 1 to 20
evens = [num for num in range(1, 21) if num % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
