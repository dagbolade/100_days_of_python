# The Number Guessing Game.
import random

from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
# ask the user for their name and store it in a variable called name.
name = input("What is your name? ").title()

# ask user for their name and store it in a variable called name, then display a welcome message to the user.

print(f"Hello {name}, I'm thinking of a number between 1 and 100.")

# import the random module and create a random number between 1 and 100, and store it in a variable called
# chosen_number.

chosen_number = random.randint(1, 100)
# print(chosen_number)

# ask the user to choose a difficulty level between 'easy' and 'hard'.
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# set the number of attempts to 0.
attempts = 0

# if the user chose 'easy', set the number of attempts to 10.
if level == "easy":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
# if the user chose 'hard', set the number of attempts to 5.
elif level == "hard":
    attempts = 3
    print(f"You have {attempts} attempts remaining to guess the number.")
# if the user chose neither 'easy' nor 'hard', display an error message.
else:
    print("Invalid input.")

# create a while loop that runs while the number of attempts is greater than 0.
while attempts > 0:
    # ask the user to guess a number and store it in a variable called guess.
    guess = int(input("Make a guess: "))
    # if the guess is equal to the chosen number, display a message to the user telling them they guessed correctly,
    # and break out of the while loop.
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
        break
    # if the guess is not equal to the chosen number, subtract 1 from the number of attempts and display a message to
    # the user telling them they guessed incorrectly.
    else:
        attempts -= 1
        # if the guess is less than the chosen number, display a message to the user telling them their guess was too
        # low or if the guess is greater than the chosen number, display a message to the user telling them their
        # guess was too high.
        if guess < chosen_number:
            print("Too low.")
        else:
            print("Too high.")
        print("Guess again.")
        # if the number of attempts is greater than 0, display a message to the user telling them how many attempts
        # they have remaining.
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
        # if the number of attempts is equal to 0, display a message to the user telling them they have run out of
        # attempts and display the chosen number.
        else:
            print(f"You've run out of guesses, you lose. The answer was {chosen_number}.")

