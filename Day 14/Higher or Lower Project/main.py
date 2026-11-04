# Higher or Lower Game Project
from art import logo, vs
from game_data import data
import random


# TODO-2: Call Randomly the Name, Follower Count, Description, and Country of A and B from dictionary
def picker(b_data):
    """Picks two random data from the dictionary, naming them A and B, respectively"""
    # TODO-6: Comparison B becomes A
    a_data = b_data
    b_data = random.choice(data)

    # TODO-3: A and B must be different
    while a_data == b_data:
        b_data = random.choice(data)

    print(f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}.")
    print(vs)
    print(f"Against B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}.")

    return  a_data, b_data
# TODO-4: Answer checker (Correct +1, Wrong End)
def checker(a_info, b_info, guess, points):
    """Compares the follower count of A and B to see which has the higher number"""
    print("\n" * 20)
    print(logo)

    a_followers = a_info['follower_count']
    b_followers = b_info['follower_count']
    if guess == "a":
        guess = a_followers
        other = b_followers
    elif guess == "b":
        guess = b_followers
        other = a_followers
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        return points, True


    if guess > other:
        print(f"You're right! Current score: {points + 1}")
        return points + 1, False
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        return points, True


def game():
    """Game proper"""
    # TODO-1: Logo
    print(logo)
    score = 0
    b_records = random.choice(data)

    game_over = False
    while not game_over:
        a_records, b_records = picker(b_records)
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        # TODO-5: Display score after each answer
        score, game_over = checker(a_records, b_records, choice, score)

game()
