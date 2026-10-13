# Rock, Paper, Scissors Game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# rock > scissors
# paper > rock
# scissors > paper

# rock (0), paper (1), scissors (2)
# if choice1 == 0 and choice2 == 2
# elif choice1 > choice2
# if choice1 == choice2

options = [rock, paper, scissors]
choice_user = input("Rock, Paper, Scissors, SHOOT!\n").lower()
choice_computer = random.choice(options)

if choice_user == "rock" and choice_computer == scissors:
    print("You Chose:\n" + rock + "\n" + "Computer Chose:\n" + scissors)
    print("You win!")
elif choice_user == "paper" and choice_computer == rock:
    print("You Chose:\n" + paper + "\n" + "Computer Chose:\n" + rock)
    print("You win!")
elif choice_user == "scissors" and choice_computer == paper:
    print("You Chose:\n" + scissors + "\n" + "Computer Chose:\n" + paper)
    print("You win!")
elif choice_user == "scissors" and choice_computer == rock:
    print("You Chose:\n" + scissors + "\n" + "Computer Chose:\n" + rock)
    print("You lose.")
elif choice_user == "rock" and choice_computer == paper:
    print("You Chose:\n" + rock + "\n" + "Computer Chose:\n" + paper)
    print("You lose.")
elif choice_user == "paper" and choice_computer == scissors:
    print("You Chose:\n" + paper + "\n" + "Computer Chose:\n" + scissors)
    print("You lose.")
elif choice_user == "rock" and choice_computer == rock:
    print("You Chose:\n" + rock + "\n" + "Computer Chose:\n" + rock)
    print("It's a draw.")
elif choice_user == "paper" and choice_computer == paper:
    print("You Chose:\n" + paper + "\n" + "Computer Chose:\n" + paper)
    print("It's a draw.")
elif choice_user == "scissors" and choice_computer == scissors:
    print("You Chose:\n" + scissors + "\n" + "Computer Chose:\n" + scissors)
    print("It's a draw.")
else:
    print("uhmmm...")