from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# create an object from the classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# create a loop that asks the user what they want
while True:
    user = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user == "off" or user == "bye":
        print("Goodbye!")
        break
    elif user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink):
            # show cost of drink
            print(f"Your drink cost: ${drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

