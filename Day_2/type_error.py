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


# exercise 2.1
# Instructions
# Write a program that adds the digits in a 2-digit number.
two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

print(first_digit + second_digit)