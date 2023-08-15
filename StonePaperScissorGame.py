## Welcome to the Stone, Paper, Scissor Game
## Rule: Rock wins against scissors; paper wins against rock; and scissors wins against paper

import random as re

print("Welcome to the GAME!")
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
game_params = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, and 2 for Scissors."))
if user_choice < 0 or user_choice > 2:
    print("Please enter a valid entry!")
else:
    print(f'User choice : {game_params[user_choice]}')
    computer_choice = re.randint(0, 2)
    print(f'Computer choice : {game_params[computer_choice]}')

    if user_choice == 0 and computer_choice == 2:
        print("User Wins!")
    elif user_choice == 1 and computer_choice == 0:
        print("User Wins!")
    elif user_choice == 2 and computer_choice == 1:
        print("User Wins!")
    elif user_choice == computer_choice:
        print("Game Draws!")
    else:
        print("Computer Wins!")