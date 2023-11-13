# Rock, Paper, Scissors game
# Displays greeting, rules, and asks for user input
print("Welcome to Rock, Paper, Scissors!")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")

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



# Displays user choice
if user_choice == "0":
  print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("Invalid input. You lose!")

# Displays computer choice
import random
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rock + "\nComputer chose: rock")
elif computer_choice == 1:
    print(paper + "\nComputer chose: paper")
elif computer_choice == 2:
    print(scissors  + "\nComputer chose: scissors")
else:
    print("Invalid input. You lose!")

# Displays winner
if user_choice == "0" and computer_choice == 2:
  print("You win!")
elif user_choice == "1" and computer_choice == 0:
    print("You win!")
elif user_choice == "2" and computer_choice == 1:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")




