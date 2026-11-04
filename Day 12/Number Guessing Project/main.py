# Number Guessing Project
import random
import art

EASY_TURNS = 10
HARD_TURNS = 5

# TODO-2: Function to set difficulty
def set_difficulty():
    """Set the number of attempts possible depending on the difficulty"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS


# TODO-4: Function to check users' guess against actual answer
def check_answer(user_guess, answer, attempts):
    """Compares the guess to the actual answer, returns number of turns"""
    if user_guess > answer:
        print("Too high.")
        return attempts - 1
    elif user_guess < answer:
        print("Too low.")
        return attempts - 1
    else:                                                       # guess == magic_number, while loop over
        print(f"You got it! The answer was {answer}")

def game():
    print(art.cooler_logo)

    # TODO-1: Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    magic_number = random.randint(1,100)
    # print(f"Psst, the correct answer is {magic_number}")

    turns = set_difficulty()

    # TODO-6: Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != magic_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        # TODO-3: Let the user guess a number
        guess = int(input("Make a guess: "))
        # TODO-5: Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, magic_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        else:
            print("Guess again.")


game()




