# blackjack.py

import random
#from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

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

def compare(user_score, computer_score, player_name, bet_amount):
    """Compare the user's score and the computer's score and return the winner"""
    if user_score == computer_score:
        return f"Draw. {player_name}'s bet of £{bet_amount} is returned."
    elif computer_score == 0:
        return f"You Lose {player_name}, opponent has Blackjack. You lose £{bet_amount}."
    elif user_score == 0:
        return f"Win with a Blackjack, congratulations {player_name}! You win £{int(bet_amount * 1.5)}."
    elif user_score > 21:
        return f"You went over. You lose £{bet_amount}."
    elif computer_score > 21:
        return f"Opponent went over. You win £{bet_amount}."
    elif user_score > computer_score:
        return f"You win £{bet_amount}, {player_name}."
    else:
        return f"You lose £{bet_amount}, {player_name}."

def get_bet():
    """Handle bets"""
    while True:
        try:
            bet = int(input("How much would you like to bet?: £ "))
            if bet <= 0:
                print("Please enter a valid amount")
            else:
                return bet
        except ValueError:
            print("Please enter a valid amount.")

def play_blackjack(player_name, bet_amount, current_balance):
    #print(logo)

    # deal the user and computer 2 cards each using deal_card() and append()
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

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
                print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
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

    # call the compare function and print the result
    result = compare(user_score, computer_score, player_name, bet_amount)

    # determine the winner and adjust the user's money
    if "You win" in result:
        current_balance += bet_amount
    elif "You Lose" in result:
        current_balance -= bet_amount

    print(result)
    return current_balance
