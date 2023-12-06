# coffee_machine project
# print a welcome message
print("Welcome to the coffee machine!")

# prompt user by asking “What would you like? (espresso/latte/cappuccino/tea/hot chocolate/milk):”

user = input("What would you like? (espresso/latte/cappuccino/tea/hot chocolate/milk): ").lower()


# todo: 2.1. check the user input to decide what to do next

# todo: 2.2. the prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

# create a function for each drink


def espresso():
    print("please insert $1.50 in coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total < 1.50:
        print("Sorry that's not enough money. Money refunded.")
    elif total > 1.50:
        change = total - 1.50
        # print(f"Here is ${change} in change in 2 decimal places.")
        print("Here is ${:.2f} in change.".format(change))
        print("Here is your espresso ☕️. Enjoy!")
    else:
        print("Here is your espresso ☕️. Enjoy!")


while True:
    user = input("What would you like? (espresso/latte/cappuccino/tea/hot chocolate/milk): ").lower()
    if user == "espresso":
        espresso()
    elif user == "latte":
        print("latte")
    elif user == "cappuccino":
        print("cappuccino")
    elif user == "tea":
        print("tea")
    elif user == "hot chocolate":
        print("hot chocolate")
    elif user == "milk":
        print("milk")
    # todo: 3. turn off the coffee machine by entering “off” to the prompt
    elif user == "off":
        print("Turning off the coffee machine...")
        break
    # todo: 4. print report
    elif user == "report":
        print("Report")
