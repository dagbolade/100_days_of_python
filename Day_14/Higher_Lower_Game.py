# Higher_Lower_Game.py
# import random
# from art import logo, vs
# from game_data import data

import random
from art import logo, vs
from game_data import data

# Display the logo
print(logo)

# Get the initial score
score = 0

# Get the first account
account_a = random.choice(data)
account_b = random.choice(data)

print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")

# Display vs
print(vs)

print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
# Ask the user to guess who has more followers
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if the user is correct or not
if account_a['follower_count'] > account_b['follower_count']:
    correct_answer = 'a'
else:
    correct_answer = 'b'

if guess == correct_answer:
    score += 1
    print(f"You're right! Current score: {score}.")
else:
    print(f"Sorry, that's wrong. Final score: {score}.")

# Get the next account using while loop so that the game continues till the user gets the answer wrong
while guess == correct_answer:
    account_a = account_b
    account_b = random.choice(data)

    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")

    # Display vs
    print(vs)

    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
    # Ask the user to guess who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the user is correct or not
    if account_a['follower_count'] > account_b['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'

    if guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")