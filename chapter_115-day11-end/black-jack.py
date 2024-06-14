import random
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    # List of possible card values in a standard Blackjack game.
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    # Randomly select and return a card from the deck.
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the total score of the given cards and checks for Blackjack and Ace adjustments."""
    # Check for a Blackjack (a hand with only two cards: Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents a Blackjack
    
    # Adjust for Aces if the total score exceeds 21.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    # Return the total score of the cards.
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the user and computer scores to determine the winner."""
    # Determine the result based on the comparison of scores.
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    """Main function to play a game of Blackjack."""
    # Display the game logo.
    print(logo)
    
    # Initialize player and dealer hands.
    user_cards = []
    computer_cards = []
    
    # Deal two cards to each player and dealer.
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # Variable to check if the game is over.
    is_game_over = False

    # Main game loop for the player.
    while not is_game_over:
        # Calculate current scores.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display player's cards and dealer's first card.
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for end of game conditions.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask player if they want another card.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Dealer's turn to draw cards until reaching at least 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display final hands and scores.
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    # Compare the final scores and print the result.
    print(compare(user_score, computer_score))

# Loop to ask the player if they want to play a new game.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    # Clear the screen (works for Windows).
    from os import system, name
    if name == 'nt':  # For Windows
        system('cls')
    else:  # For macOS and Linux (name is 'posix')
        system('clear')
    
    # Start a new game.
    play_game()
