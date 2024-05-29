# Define a dictionary with programming terms and their definitions
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again."
}

# Print the initial dictionary
print(programming_dictionary)

# Add a new term 'Loop' to the dictionary with its definition
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Print the dictionary after adding the new term
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# loop through a dictionary 
for thing in (programming_dictionary):
    print("looping the dictionary\n" + thing)

# Define an empty dictionary
empty_dictionary = {}

# Clear the programming dictionary by assigning it to an empty dictionary
programming_dictionary = {}

# Print the now-empty programming dictionary
print(programming_dictionary)
