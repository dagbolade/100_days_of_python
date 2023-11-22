# calculator

# Creating a basic calculator using python

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# store the functions in a dictionary as operators and values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# ask the user for input
def calculator():
    # ask the user for input
    num1 = float(input("What is the first number?: "))
    for operator in operations:
        print(operator)
    # ask the user if they want to continue
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # ask the user if they want to continue
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
