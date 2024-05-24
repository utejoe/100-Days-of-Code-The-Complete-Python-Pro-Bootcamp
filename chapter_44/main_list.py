# List of states of America
states_of_america = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New Hampshire", "New Jersey", "New Mexico", "New York", 
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
    "West Virginia", "Wisconsin", "Wyoming"
]

# Print the first state in the list
print(states_of_america[0]) # Output: Alabama

# Print the second state in the list
print(states_of_america[1]) # Output: Alaska

# Print the last state in the list
print(states_of_america[-1]) # Output: Wyoming

# Replace the second state in the list with "Pencilvania"
states_of_america[1] = "Pencilvania"

# Add a new state "Lagos" to the end of the list
states_of_america.append("Lagos")

# Extend the list by adding multiple new states at the end
states_of_america.extend(["abuja", "benin", "europe"])

# Count the number of states in the list
number_of_states = len(states_of_america)
print(f"Number of states: {number_of_states}") # Output the number of states

# Print the updated list of states
print(states_of_america)
