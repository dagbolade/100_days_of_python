# coffee_machine project
# print a welcome message
from menu import MENU, resources

print("Welcome to the coffee machine!")


# prompt user by asking “What would you like? (espresso/latte/cappuccino/tea/hot chocolate/milk):”
def prompt_user():
    user = input("What would you like? (espresso/latte/cappuccino/tea/hot chocolate/milk): ").lower()
    return user


money = 0


# create functions for the calculations
def calculate_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    return total


# create functions for the drinks
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
        add_money()
    else:
        print("Here is your espresso ☕️. Enjoy!")
        add_money()
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
        add_money()
    else:
        print("Here is your latte ☕️. Enjoy!")
        add_money()

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
        add_money()
    else:
        print("Here is your cappuccino ☕️. Enjoy!")
        add_money()
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
        add_money()
    else:
        print("Here is your tea ☕️. Enjoy!")
        add_money()
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
        add_money()

    else:
        print("Here is your hot chocolate ☕️. Enjoy!")
        add_money()

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
        add_money()
    else:
        print("Here is your milk ☕️. Enjoy!")
        add_money()

    return milk

# create a function to add the money to the money variable and return the money as a float
def add_money():
    global money
    money += MENU[user]["cost"]
    return money

# create a function for report
def report():
    print("Report")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Tea: {resources['tea']}g")
    print(f"Chocolate: {resources['chocolate']}g")
    print(f"Money: ${money}")
    return report


# # create a function to check if there are enough resources to make the drink
def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# the prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show
# again to serve the next customer.
while True:
    #  check the user input to decide what to do next
    user = prompt_user()
    if user == "espresso":
        check_resources(user)
        espresso()

    elif user == "latte":
        check_resources(user)
        latte()

    elif user == "cappuccino":
        check_resources(user)
        cappuccino()

    elif user == "tea":
        check_resources(user)
        tea()

    elif user == "hot chocolate":
        check_resources(user)
        hot_chocolate()

    elif user == "milk":
        check_resources(user)
        milk()

    # turn off the coffee machine by entering “off” to the prompt
    elif user == "off":
        print("Turning off the coffee machine...")
        break
    # todo: 4. print report
    elif user == "report":
        report()
