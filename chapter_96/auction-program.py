# Step 1: Import necessary modules and set up initial variables
import os

# Function to clear the console
def clear():
    # Check if the system is Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Otherwise, assume it is a Unix-based system (Linux/Mac)
    else:
        _ = os.system('clear')

# ASCII art for the auction logo
auction_logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | '-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""

# Dictionary to store the bids
bids = {}

# Step 2: Define the function to find the highest bid
def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# Step 3: Create the main loop for collecting bids
def auction():
    print(auction_logo)
    print("Welcome to the blind auction program.")
    bidding_finished = False

    while not bidding_finished:
        # Get user input for name and bid
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        
        # Add the bid to the bids dictionary
        bids[name] = bid
        
        # Ask if there are other bidders
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if should_continue == "no":
            bidding_finished = True
        elif should_continue == "yes":
            clear()
    
    # Step 4: Find and display the highest bid
    find_highest_bid(bids)

# Run the auction program
auction()
