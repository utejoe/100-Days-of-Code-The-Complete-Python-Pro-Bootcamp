import random

# Sample names_string, assuming this variable is defined somewhere in your code
names_string = "Alice, Bob, Charlie, David, Eva"  # Example string of names

# Split the names_string into a list of names
names = names_string.split(", ")

# Get the total number of items in the list
num_items = len(names)

# Generate a random index between 0 and the last index of the list
random_choice = random.randint(0, num_items - 1)

# Select a random name from the list using the random index
random_name = names[random_choice]

# Print the randomly selected name
print(random_name)
