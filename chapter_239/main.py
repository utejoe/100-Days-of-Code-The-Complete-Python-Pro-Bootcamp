import pandas as pd

# Example lists of all US states and guessed states
all_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
guessed_states = ["California", "Texas", "Florida", "New York"]

while True:
    # Get input from the user
    user_input = input("Enter a state name (or 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        # Using list comprehension to find the missing states
        missing_states = [state for state in all_states if state not in guessed_states]

        # Save the missing states to a CSV file
        missing_states_df = pd.DataFrame(missing_states, columns=["Missing States"])
        missing_states_df.to_csv("missing_states.csv", index=False)

        print("Missing states saved to 'missing_states.csv'.")
        break
    elif user_input in all_states:
        guessed_states.append(user_input)
        print(f"{user_input} added to guessed states.")
    else:
        print(f"{user_input} is not a valid US state.")

# Continue with the rest of the game logic if needed
