import random

def deal_card():
    """Returns a random card from the deck."""
    # Deck of cards, where 10 is repeated for 10, Jack, Queen, and King, and 11 represents Ace
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    # Randomly choose a card from the deck and return it
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the total score of the given cards."""
    # Check for Blackjack (a hand with only two cards: Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 will be used to represent Blackjack
    # Handle the case where there is an Ace (11) and the total score is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # Return the sum of the cards
    return sum(cards)

def compare(player_score, dealer_score):
    """Compares the scores and returns the result of the game."""
    # Compare player and dealer scores and return the appropriate result message
    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_blackjack():
    """Main function to play a game of Blackjack."""
    # Display the game logo
    print(logo)
    
    # Initialize player and dealer hands
    player_cards = []
    dealer_cards = []
    
    # Deal two cards to each player and dealer
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    # Variable to check if the game is over
    game_over = False
    
    # Main game loop for the player
    while not game_over:
        # Calculate current scores
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        
        # Display player's cards and dealer's first card
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        
        # Check for end of game conditions
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            # Ask player if they want another card
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True
    
    # Dealer's turn to draw cards until reaching at least 17
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    
    # Display final hands and scores
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    # Compare the final scores and print the result
    print(compare(player_score, dealer_score))

# ASCII art for the game logo
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |
      `------'                           |__/
"""

# Loop to ask the player if they want to play a new game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_blackjack()
