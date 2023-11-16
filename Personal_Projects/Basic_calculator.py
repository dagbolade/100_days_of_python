# Creating a basic calculator using python

# display greetings
print("Welcome to the basic calculator")
name = input("Enter your name: ")
print("Hello " + name + ", please enter the following details")

# get the first number
num1 = float(input("Enter the first number you wish to calculate: "))
# get the second number
num2 = float(input("Enter the second number you wish to calculate: "))

# get the operator

operator = input("Enter the operator you wish to use +, -, * or X, / : ")

# calculate the result

if operator == "+":
    result = num1 + num2
    # display the result
    print("Hi, " + name + " The result is " + str(result))
elif operator == "-":
    result = num1 - num2
    # display the result
    print("Hi, " + name + " The result is " + str(result))
elif operator == "*" or operator == "X":
    result = num1 * num2
    # display the result
    print("Hi, " + name + " The result is " + str(result))
elif operator == "/":
    result = num1 / num2
    # display the result
    print("Hi, " + name + " The result is " + str(result))
else:
    print("Invalid operator")



