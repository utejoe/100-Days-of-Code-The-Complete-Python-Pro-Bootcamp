# Import necessary modules and data
from art import logo
from game_data import data
import random
from replit import clear

# Function to format and print account data
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    formatted_data = f"{name}, a {description}, from {country}."
    return formatted_data

# Function to check user's guess
def check_answer(guess, a_followers, b_followers):
    """Check if the user's guess is correct."""
    if guess == "a":
        return a_followers > b_followers
    elif guess == "b":
        return b_followers > a_followers
    else:
        print("Invalid input. You must type 'A' or 'B'.")
        return False

# Main game loop
game_should_continue = True
score = 0

while game_should_continue:
    # Clear the screen and display logo
    clear()
    print(logo)
    
    # Generate random accounts
    account_a = random.choice(data)
    account_b = random.choice(data)

    while account_a == account_b:  # Ensure different accounts
        account_b = random.choice(data)
    
    # Format and print account data
    print("Compare A:")
    print(format_data(account_a))
    print("vs")
    print("Compare B:")
    print(format_data(account_b))
    
    # Ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    # Check user's guess
    is_correct = check_answer(guess, a_followers, b_followers)

    # Provide feedback and update score
    if is_correct:
        print("You're right!")
        score += 1
    else:
        print("Sorry, that's wrong.")
        print(f"Your final score is {score}.")
        game_should_continue = False  # End game loop

    # Pause before next round
    input("Press Enter to continue...")

# End of game
