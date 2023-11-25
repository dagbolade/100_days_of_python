# The Number Guessing Game.
import random
#from art import logo

#print(logo)


def welcome_user():
    """Welcome the user and ask for their name."""
    name = input("What is your name? ").title()
    print(f"Hello {name}, I'm thinking of a number between 1 and 100.")


def choose_difficulty():
    """Ask the user to choose a difficulty level."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return 10 if level == "easy" else 5 if level == "hard" else 0


def play_number_guessing_game(chosen_number, attempts, bet):
    """Play the Number Guessing Game."""
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == chosen_number:
            print(f"You got it! The answer was {chosen_number}.")
            break
        else:
            attempts -= 1
            print("Too low." if guess < chosen_number else "Too high.")
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.") if attempts > 0 else print(
                f"You've run out of guesses, you lose. The answer was {chosen_number}.")


# Get the bet amount from the user
bet_amount_guessing_game = int(input("How much would you like to bet in the Number Guessing Game?: £ "))

# Welcome the user and set up the game
welcome_user()
chosen_number = random.randint(1, 100)
attempts = choose_difficulty()

# Play the Number Guessing Game
if attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    play_number_guessing_game(chosen_number, attempts, bet_amount_guessing_game)
