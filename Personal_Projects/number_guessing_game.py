# number_guessing_game.py
import random

def welcome_user(player_name):
    """Welcome the user and ask for their name."""
    print(f"Hello {player_name}, I'm thinking of a number between 1 and 100.")

def choose_difficulty():
    """Ask the user to choose a difficulty level."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return 5 if level == "easy" else 3 if level == "hard" else 0

def play_game(player_name, bet_amount, current_balance):
    """Play the Number Guessing Game."""
    while True:
        chosen_number = random.randint(1, 100)
        attempts = choose_difficulty()

        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")

            while attempts > 0:
                guess = int(input("Make a guess: "))
                if guess == chosen_number:
                    print(f"You got it! The answer was {chosen_number}.")
                    print(f"Congratulations {player_name}, you win £{bet_amount * 2}.")
                    return current_balance + bet_amount * 2
                else:
                    attempts -= 1
                    print("Too low." if guess < chosen_number else "Too high.")
                    print("Guess again.")
                    print(f"You have {attempts} attempts remaining to guess the number.") if attempts > 0 else print(
                        f"You've run out of guesses, you lose. The answer was {chosen_number}.")

            print(f"You've run out of attempts. The answer was {chosen_number}.")
            current_balance -= bet_amount
            print(f"Your new balance: £{current_balance}")

            play_again = input("Do you want to play again? Type 'y' to play again or any other key to return to the main menu: ").lower()
            if play_again != 'y':
                return current_balance
        else:
            print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
