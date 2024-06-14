# Bug Code: Fixing Errors in the Editor

# Take user input for age
age = input("Enter your age: ")

# Check if the age is greater than 18
if age > 18:  # Error: Expected an indented block
    print("You are an adult")

# Check if the age is greater than 18
if age > 18:  # Error: TypeError: '>' not supported between instances of 'str' and 'int'
    print("You are an adult")
