# def greet():
#     print("Hi  David")
#     print("Welcome aboard")
#     print("nice to meet you")
#
#
# greet()
#
#
# # Functions with parameters
#
# def greet(name):
#     print(f"Hi {name}")
#     print("Welcome aboard")
#     print(f"nice to meet you {name}")
#
#
# greet("David")

# Functions with multiple parameters
def greet(name, location):
    print(f"Hi {name}")
    print(f"Welcome aboard {name}")
    print(f"you are from {location}")


greet("David", "London")


# keyword arguments

def greet(name, location):
    print(f"Hi {name}")
    print(f"Welcome aboard {name}")
    print(f"you are from {location}")


greet(name=" Dami ", location="London")
