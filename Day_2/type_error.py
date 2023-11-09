# Type Error, Type Checking, Type Conversion
num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.")
# TypeError: can only concatenate str (not "int") to str

# To fix this error, we need to convert the num_char variable into a string.
# We can do this by wrapping the variable with str().

# Type Checking
print(type(num_char))
