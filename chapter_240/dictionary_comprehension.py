# Dictionary of state populations
state_population = {
    "Alabama": 4903185,
    "Alaska": 731545,
    "Arizona": 7278717,
    "Arkansas": 3017804,
    "California": 39512223,
    "Colorado": 5758736,
    # ... other states
}

# List of guessed states
guessed_states = ["California", "Texas", "Florida", "New York"]

# Dictionary comprehension to create a new dictionary with guessed states and their populations
guessed_state_population = {state: state_population[state] for state in guessed_states if state in state_population}
print(guessed_state_population)  # Output: {'California': 39512223}
