import random

# Define the values of the cards
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  # Aces can be 1 or 11; we'll handle that logic separately
}

# Create a deck of cards
def create_deck():
    deck = []
    for card in CARD_VALUES.keys():
        deck.extend([card] * 4)  # 4 cards of each type
    random.shuffle(deck)
    return deck

# Calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        value += CARD_VALUES[card]
        if card == "A":
            ace_count += 1
    # Adjust for Aces if necessary
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

# Deal two cards to a player or dealer
def deal_initial_hand(deck):
    return [deck.pop(), deck.pop()]

# Display the current hand
def display_hand(player, hand):
    print(f"{player}'s hand: {', '.join(hand)} (Value: {calculate_hand_value(hand)})")

# Player's turn
def player_turn(deck, player_hand):
    while True:
        display_hand("Player", player_hand)
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                display_hand("Player", player_hand)
                print("You busted!")
                return player_hand
        elif choice == 'stand':
            break
        else:
            print("Invalid input, please type 'hit' or 'stand'.")
    return player_hand

# Dealer's turn
def dealer_turn(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    display_hand("Dealer", dealer_hand)
    return dealer_hand

# Main function to play the game
def play_blackjack():
    deck = create_deck()
    player_hand = deal_initial_hand(deck)
    dealer_hand = deal_initial_hand(deck)

    # Show the dealer's first card
    print(f"Dealer's visible card: {dealer_hand[0]}")

    # Player's turn
    player_hand = player_turn(deck, player_hand)

    # Check if player busted
    if calculate_hand_value(player_hand) > 21:
        print("Dealer wins!")
        return

    # Dealer's turn
    dealer_hand = dealer_turn(deck, dealer_hand)

    # Check if dealer busted
    if calculate_hand_value(dealer_hand) > 21:
        print("Dealer busted! You win!")
        return

    # Compare hands to determine the winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    print(f"\nFinal Results: Player: {player_value}, Dealer: {dealer_value}")
    if dealer_value > player_value:
        print("Dealer wins!")
    elif player_value > dealer_value:
        print("You win!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_blackjack()
