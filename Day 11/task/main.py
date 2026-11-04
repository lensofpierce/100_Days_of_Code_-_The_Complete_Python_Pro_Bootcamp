import random
import art


def deal_card():
    """Draw a random card to be added to the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_drawn = random.choice(cards)
    return card_drawn


def calculate_score(player_cards):
    """Takes the list of cards and gets its total score by its sum"""
    if sum(player_cards) == 21 and len(player_cards) == 2:         # Blackjack
        return 0

    if 11 in player_cards and sum(player_cards) > 21:           # Ace over 21
        player_cards.remove(11)
        player_cards.append(1)

    return sum(player_cards)


def compare(u_score, c_score):          # Compare the user (u) score and computer (c) score
    """Compare the scores and winning/losing conditions between the user and the computer"""
    if u_score == c_score:
        return "It's a draw."
    elif c_score == 0:
        return "Computer has a blackjack. You lose."
    elif u_score == 0:
        return "You have a blackjack. You win!"
    elif u_score > 21:
        return "You went over 21. You lose."
    elif c_score > 21:
        return "Computer went over 21. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose."


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1         # To avoid similarity with Blackjack score condition
    computer_score = -1         # To avoid similarity with Blackjack score condition
    game_over = False

    for draw in range(2):           # Draw the first 2 cards for user and computer
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:            # Loop for the player's turn to keep on dealing a card
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or user_score == 21:
            game_over = True
        else:
            draw_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_new_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final tally
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


