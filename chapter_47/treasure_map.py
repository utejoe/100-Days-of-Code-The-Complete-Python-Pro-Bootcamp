# Initial map setup
line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]

# Function to print the map
def print_map(map):
    for line in map:
        print(line)

# Print the initial map
print_map(map)

# Example input
position = input("Where do you want to put the treasure? ")

# Extracting the input details
letter = position[0].lower()  # e.g., 'B'
number = position[1]  # e.g., '2'

# Convert letter to index (a, b, c -> 0, 1, 2)
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)

# Convert number to index (1, 2, 3 -> 0, 1, 2)
number_index = int(number) - 1

# Mark the spot with an 'X'
map[number_index][letter_index] = "X"

# Print the modified map
print_map(map)
