# Day 11
# BlackJack Capstone Project
# Description: A simple BlackJack game
# Author: David Agbolade

import random


# create a list of cards
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# get user_name
name = input("What is your name?: ").title()

# display greetings
print(f"Welcome to the BlackJack game, {name}!, ARE YOU READY TO PLAY?!!!")

print("The goal of the game is to get as close to 21 as possible, without going over 21")
print("Cards 2 to 10 have their face values, J, Q and K are worth 10 and Ace is worth 11 or 1")
print("The computer will deal you and itself 2 cards each")
print("You can choose to draw another card or pass")
print("If you go over 21, you lose")
print("If you get 21, you win")
print("If you get a score higher than the computer, you win")
print("If the computer gets a score higher than you, you lose")
print("If you and the computer get the same score, it's a draw")
print("Let's get started, shall we?")
print("Your first 2 cards are: ")

# deal the user and computer 2 cards each using deal_card() and append()
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)


# create a function to calculate the score that takes a list of cards as input
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # check for blackjack i.e. if the user or computer has a score of 21
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # check for an 11 and replace it with a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # return the sum of the cards
    return sum(cards)


# if the computer or user has a blackjack i.e. a score of 21 with 2 cards
# then the game ends

# create a variable to keep track of whether the game has ended
is_game_over = False

# if the game has not ended, ask the user if they want to draw another card
# if yes, deal another card and add to the user's card list
# if no, then the game ends

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        # ask the user if they want to draw another card
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

# once the user is done drawing cards, the computer starts drawing cards
# the computer should keep drawing cards until it has a score greater than 17
# once the computer has a score greater than 17, the game ends

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")


# create a function to compare the user's score and the computer's score
def compare(user_score, computer_score):
    """Compare the user's score and the computer's score and return the winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


# call the compare function and print the result
print(compare(user_score, computer_score))

# ask the user if they want to play again
# if yes, start the game again
