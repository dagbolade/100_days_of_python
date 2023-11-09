# # Type Error, Type Checking, Type Conversion
# num_char = len(input("What is your name? "))
# # print("Your name has " + num_char + " characters.")
# # TypeError: can only concatenate str (not "int") to str
# # This error occurs because we are trying to concatenate a string with an integer.
#
# # Type Checking
# print(type(num_char))
#
# # Type Conversion
# # To fix this error, we need to convert the num_char variable into a string.
# # We can do this by wrapping the variable with str().
#
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))
b = str(a)
print(type(b))
c = float(a)
print(type(c))
