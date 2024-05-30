import os

# Function to clear the console
def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (os.name is 'posix')
    else:
        os.system('clear')

from art import logo

# Dictionary to store the bids
bids = {}

# Function to find the highest bid
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# Main auction function
def auction():
    print(logo)
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
    
    # Find and display the highest bid
    find_highest_bidder(bids)

# Run the auction program
auction()
