# Nested if else statements
print("Welcome to the rollercoaster!")
# convert input to integer
height = int(input("What is your height in cm?"))
# create the bill variable
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    # Nested if else statements
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("Adults ticket are $12.")
    interested = input("Do you want a photo taken? Y or N.")
    if interested == "Y":
        print("Photo costs $3")
        bill += 3
    else:
        print("No problem.")

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# # # # Instructions
# # bmi 2.0
# # Instructions
# # Enter your height in meters e.g., 1.55
# height = float(input("enter your height in m:"))
# # Enter your weight in kilograms e.g., 72
# weight = int(input("enter your weight in kg:"))
# # 🚨 Don't change the code above 👆
# # under 18.5 they are underweight
# # Over 18.5 but below 25 they have a normal weight
# # Equal to or over 25 but below 30 they are slightly overweight
# # Equal to or over 30 but below 35 they are obese
# # Equal to or over 35 they are clinically obese.
# # Write your code below this line 👇
# bmi = weight / height ** 2
#
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif 18.5 < bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif 25 <= bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif 30 <= bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")
