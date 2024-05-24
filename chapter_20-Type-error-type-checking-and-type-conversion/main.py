# Prompt the user to input their name, calculate the length of the input string (the name), 
# and store the length in the variable 'num_char'
num_char = len(input("What is your name?\n"))

# Print the data type of the variable 'num_char' (should be an integer)
print(type(num_char))

# Convert the integer value of 'num_char' to a string and store it in the variable 'new_num_char'
new_num_char = str(num_char)

# Print a message indicating the number of characters in the user's name
print("Your name has " + new_num_char + " characters.")

# Convert the string '123' to a floating-point number and store it in the variable 'a'
a = float('50')

# Print the data type of the variable 'a' (should be a float)
print(type(a))

c = "Uyi"

# Add the float value of 'a' (123.0) to the integer 70 and print the result
print(70 + a)
print(c + ' is ' + str(120) + " years old")
