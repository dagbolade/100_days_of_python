# Describe the problem

# Debugging
# Describe Problem
# def my_function():
#     for i in range(1, 20):  # range(1, 20) -> range(1, 21)
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# Reproduce the Bug
# from random import randint
#
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]  # dice_imgs[6] -> dice_imgs[5]
# dice_num = randint(1, 6) # or randint(0, 5)
# print(dice_imgs[dice_num - 1])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year <= 1993:  # year >= 1981 and year <= 1993
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you? ") # int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
