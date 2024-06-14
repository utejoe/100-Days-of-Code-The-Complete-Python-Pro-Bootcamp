# Fixed Code: Debugging with Logical Evaluation

# Take user input for year of birth
year = int(input("Enter your year of birth: "))

# Check if the user is a millennial or Gen Z based on their birth year
if year >= 1980 and year <= 1994:  # Adjusted conditions to include 1994
    print("You are a millennial")
elif year > 1994:
    print("You are Gen Z")
