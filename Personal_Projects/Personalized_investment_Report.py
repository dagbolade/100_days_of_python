# Personalized investment Report Project
# display a welcome message
print("Welcome to the Personalized Investment Report App")

# get the user real name
name = input("What is your name? \n")

# get the user age
age = int(input("What is your age? \n"))

# get the user initial investment, expected annual interest rate as a percentge and the number of years for the
# investment.
initial_investment = float(input("What is your initial investment? \n"))
interest_rate = float(input("What is your expected annual interest rate? \n"))
years = int(input("How many years will you be investing for? \n"))

# calculate the future value of the investment
# future_value = initial_investment * (1 + interest_rate / 100) ** years
future_value = initial_investment

# generate the investment report
print("Investment Report for " + name)
# use a loop to calculate the value of the investment at the end of each year
for i in range(1, years + 1):

    future_value = future_value * (1 + interest_rate / 100)
    print(f"Year {i}: £{future_value:.2f}")

# present the starting conditions and a yearly report of the investment
print(f"Initial Investment: £{initial_investment:.2f}")
print(f"Annual Interest Rate: {interest_rate}%")
print(f"Years Invested: {years}")
print(f"Future Value: £{future_value:.2f}")
print("Goodbye and Thank you!")
