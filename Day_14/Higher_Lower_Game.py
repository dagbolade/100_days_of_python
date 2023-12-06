# Higher_Lower_Game.py
# import random
# from art import logo, vs
# from game_data import data

# import random
# from art import logo, vs
# from game_data import data
#
# # Display the logo
# print(logo)
#
# # Get the initial score
# score = 0
#
# # Get the first account
# account_a = random.choice(data)
# account_b = random.choice(data)
#
# print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
#
# # Display vs
# print(vs)
#
# print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
# # Ask the user to guess who has more followers
# guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#
# # Check if the user is correct or not
# if account_a['follower_count'] > account_b['follower_count']:
#     correct_answer = 'a'
# else:
#     correct_answer = 'b'
#
# if guess == correct_answer:
#     score += 1
#     print(f"You're right! Current score: {score}.")
# else:
#     print(f"Sorry, that's wrong. Final score: {score}.")
#
# # Get the next account using while loop so that the game continues till the user gets the answer wrong
# while guess == correct_answer:
#     account_a = account_b
#     account_b = random.choice(data)
#
#     print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
#
#     # Display vs
#     print(vs)
#
#     print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
#     # Ask the user to guess who has more followers
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#
#     # Check if the user is correct or not
#     if account_a['follower_count'] > account_b['follower_count']:
#         correct_answer = 'a'
#     else:
#         correct_answer = 'b'
#
#     if guess == correct_answer:
#         score += 1
#         print(f"You're right! Current score: {score}.")
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}.")

# now using a function
import random
from art import logo, vs

from game_data import data


def get_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account data into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display the logo
print(logo)

# Get the initial score
score = 0

# Get the first account
account_a = get_account()
account_b = get_account()

# Make the game repeatable
game_should_continue = True

while game_should_continue:
    # Make account at position B become the next account at position A
    account_a = account_b
    account_b = get_account()

    while account_a == account_b:
        account_b = get_account()

    print(f"Compare A: {format_data(account_a)}.")

    # Display vs
    print(vs)

    print(f"Against B: {format_data(account_b)}.")

    # Ask the user to guess who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if the user is correct or not
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    print("\033c")

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
