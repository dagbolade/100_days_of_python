# Love Calculator Project
# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

print("Welcome to the Love Calculator!")
print("The Love Calculator is calculating your love score....")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# convert to lower case
name1_lower = name1.lower()
name2_lower = name2.lower()
# create a variable to store both names

combined_names = name1_lower + name2_lower
# count the number of times TRUE occurs
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
# count the number of times LOVE occurs
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
# add the two counts together
true = t + r + u + e
love = l + o + v + e
# convert to string
true_str = str(true)
love_str = str(love)
# combine the two strings
score = true_str + love_str
# convert to integer
score_int = int(score)
# print the score
print(f"Your love score is {score_int}")
# if else statements
if (score_int < 10) or (score_int > 90):
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif 40 >= score_int <= 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")
