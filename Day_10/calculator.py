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
num1 = int(input("What is the first number?: "))


for operator in operations:
    print(operator)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What is the second number?: "))
# get the function from the dictionary
calculation_function = operations[operation_symbol]
# calculate the result
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")