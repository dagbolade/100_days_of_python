# print("Welcome to the rollercoaster!")
# # convert input to integer
# height = int(input("What is your height in cm?"))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#
#

# # Odd or Even
# # Instructions
# # Write a program that works out whether if a given number is an odd or even number.
#
# # Even numbers can be divided by 2 with no remainder.
# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆
x = number % 2
# Write your code below this line 👇
if x == 0 :
  print("This is an even number.")
else:
  print("This is an odd number.")