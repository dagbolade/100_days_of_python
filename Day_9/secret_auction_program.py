# secret auction program
import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

# empty dictionary to store the name and bid of the bidder
bidders = {}


# ask user for name and bid
def ask_bidder():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid


# ask user if there are other bidders
def other_bidder():
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other == "yes":
        clear.clear()
        return True
    else:
        return False


# check for the highest bidder
def highest_bidder(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# ask for the first bidder
ask_bidder()
# ask if there are other bidders
while other_bidder():
    ask_bidder()
# check for the highest bidder
highest_bidder(bidders)
