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
# age = int(input("How old are you? ")) # int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.") # wrong print("You can drive at age {age}.")

# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # == instead of =
# # add a print statement to check the values of pages and word_per_page
# print(pages, word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger like pythontutor.com, thonny ide, or pycharm

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Day 13 Project: Debugging Caesar Cipher
