# coffee_machine project
# print a welcome message
print("Welcome to the coffee machine!")


# prompt user by asking “What would you like? (espresso/latte/cappuccino/tea/hot chocolate/milk):”
def prompt_user():
    user = input("What would you like? (espresso/latte/cappuccino/tea/hot chocolate/milk): ").lower()
    return user


# create functions for the calculations
def calculate_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


#  check the user input to decide what to do next


# create a function for each drink

def espresso():
    print("please insert $1.50 in coins")
    total = calculate_money()
    if total < 1.50:
        print("Sorry that's not enough money. Money refunded.")
    elif total > 1.50:
        change = total - 1.50
        # print(f"Here is ${change} in change in 2 decimal places.")
        print("Here is ${:.2f} in change.".format(change))
        print("Here is your espresso ☕️. Enjoy!")
    else:
        print("Here is your espresso ☕️. Enjoy!")
    return espresso


def latte():
    print("please insert $2.50 in coins")
    total = calculate_money()
    if total < 2.50:
        print("Sorry that's not enough money. Money refunded.")
    elif total > 2.50:
        change = total - 2.50
        # print(f"Here is ${change} in change in 2 decimal places.")
        print("Here is ${:.2f} in change.".format(change))
        print("Here is your latte ☕️. Enjoy!")
    else:
        print("Here is your latte ☕️. Enjoy!")
    return latte


def cappuccino():
    print("please inert $3.00 in coins")
    # then call the calculate_money function
    total = calculate_money()
    if total < 3.00:
        print("Sorry that's not enough money. Money refunded.")
    elif total > 3.00:
        change = total - 3.00
        # print(f"Here is ${change} in change in 2 decimal places.")
        print("Here is ${:.2f} in change.".format(change))
        print("Here is your cappuccino ☕️. Enjoy!")
    else:
        print("Here is your cappuccino ☕️. Enjoy!")
    return cappuccino


def tea():
    print("please insert $1.50 in coins")
    total = calculate_money()
    if total < 1.50:
        print("Sorry that's not enough money. Money refunded.")
    elif total > 1.50:
        change = total - 1.50
        # print(f"Here is ${change} in change in 2 decimal places.")
        print("Here is ${:.2f} in change.".format(change))
        print("Here is your tea ☕️. Enjoy!")
    else:
        print("Here is your tea ☕️. Enjoy!")
    return tea


def hot_chocolate():
    print("please insert $2.50 in coins")
    total = calculate_money()
    if total < 2.50:
        print("Sorry that's not enough money. Money refunded.")
    elif total > 2.50:
        change = total - 2.50
        # print(f"Here is ${change} in change in 2 decimal places.")
        print("Here is ${:.2f} in change.".format(change))
        print("Here is your hot chocolate ☕️. Enjoy!")
    else:
        print("Here is your hot chocolate ☕️. Enjoy!")
    return hot_chocolate


def milk():
    print("please insert $1.00 in coins")
    total = calculate_money()
    if total < 1.00:
        print("Sorry that's not enough money. Money refunded.")
    elif total > 1.00:
        change = total - 1.00
        # print(f"Here is ${change} in change in 2 decimal places.")
        print("Here is ${:.2f} in change.".format(change))
        print("Here is your milk ☕️. Enjoy!")
    else:
        print("Here is your milk ☕️. Enjoy!")
    return milk


# the prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show
# again to serve the next customer.

while True:
    user = prompt_user()
    if user == "espresso":
        espresso()
    elif user == "latte":
        latte()
    elif user == "cappuccino":
        print("cappuccino")
    elif user == "tea":
        tea()
    elif user == "hot chocolate":
        hot_chocolate()
    elif user == "milk":
        milk()
    # todo: 3. turn off the coffee machine by entering “off” to the prompt
    elif user == "off":
        print("Turning off the coffee machine...")
        break
    # todo: 4. print report
    elif user == "report":
        print("Report")
