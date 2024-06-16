# Given input (for example purposes, replace with actual input string from Line 1)
input_string = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

# Step 1: Split the input string into a list of strings
list_of_strings = input_string.split(', ')

# Step 2: Convert the list of strings to a list of integers using list comprehension
numbers = [int(x) for x in list_of_strings]

# Step 3: Filter the even numbers using list comprehension
result = [num for num in numbers if num % 2 == 0]

# Print the result to check the code
print(result)
