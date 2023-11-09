# number manipulations
score = 0
height = 1.9
isWinning = True

# f-string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# exercise 2.3
# Instructions
# Your life in weeks
age = input("What is your current age? ")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
# # or
# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# weeks_in_a_year = 52
# weeks_in_90_years = 4680
# get_current_age_in_weeks = int(age) * weeks_in_a_year
# weeks_user_have_left_till_90 = weeks_in_90_years - get_current_age_in_weeks
#
# print(f"You have {weeks_user_have_left_till_90} weeks left.")
