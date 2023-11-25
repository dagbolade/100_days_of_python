# Main Script

from blackjack import play_blackjack
from number_guessing_game import play_number_guessing_game

def get_initial_balance():
    """Prompt the user for their initial balance."""
    while True:
        try:
            balance = int(input("Enter your initial balance: £ "))
            if balance < 0:
                print("Please enter a valid amount.")
            else:
                return balance
        except ValueError:
            print("Please enter a valid amount.")

def get_player_name():
    """Prompt the user for their name."""
    return input("What is your name?: ").title()

def select_game():
    """Prompt the user to select a game."""
    while True:
        try:
            game_choice = int(input("Select a game:\n1. Blackjack\n2. Number Guessing Game\nEnter the corresponding number: "))
            if game_choice not in [1, 2]:
                print("Please enter a valid choice.")
            else:
                return game_choice
        except ValueError:
            print("Please enter a valid choice.")

def main():
    # Get the initial balance and player name from the user
    initial_balance = get_initial_balance()
    player_name = get_player_name()
    current_balance = initial_balance

    while True:
        # Display current balance
        print(f"{player_name}, your current balance: £ {current_balance}")

        # Select the game
        game_choice = select_game()

        if game_choice == 1:
            # Blackjack
            bet_amount_blackjack = int(input("How much would you like to bet in Blackjack?: £ "))
            current_balance = play_blackjack(player_name, bet_amount_blackjack, current_balance)
        elif game_choice == 2:
            # Number Guessing Game
            bet_amount_guessing_game = int(input("How much would you like to bet in the Number Guessing Game?: £ "))
            current_balance = play_number_guessing_game(player_name, bet_amount_guessing_game, current_balance)

        # Ask if the player wants to continue playing
        play_again = input("Do you want to play another game? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            print(f"Thanks for playing, {player_name}! Your final balance: £ {current_balance}")
            break

if __name__ == "__main__":
    main()
