# Print a welcome message to the user
print("Welcome to the rollercoaster!")

# Ask the user for their height in centimeters and convert the input to an integer
height = int(input("What is your height in cm? "))

# Check if the user's height is 120 cm or more
if height >= 120:
    # If the height is sufficient, print a message allowing them to ride
    print("You can ride the rollercoaster!")
    
    # Ask the user for their age in years and convert the input to an integer
    age = int(input("What is your age in years? "))
    
    # Check if the user is younger than 12 years old
    if age < 12:
        # If the user is under 12, inform them of the ticket price
        print("Please pay $5.")
    
    # Check if the user is between 12 and 18 years old (inclusive)
    elif age <= 18:
        # If the user is between 12 and 18, inform them of the ticket price
        print("Please pay $7.")
    
    # If the user is older than 18 years
    else:
        # Inform them of the adult ticket price
        print("Please pay $12.")
else:
    # If the height is less than 120 cm, inform the user that they cannot ride
    print("Sorry, you have to grow taller before you can ride.")
