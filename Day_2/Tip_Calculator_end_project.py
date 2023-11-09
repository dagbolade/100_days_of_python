# Tip calculator Project.
# display a welcome message
print("Welcome to the tip calculator.")

# ask the user for the total bill
total_bill = float(input("What was the total bill? £"))

# ask the user for the percentage tip they want to give

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# ask the user for the number of people to split the bill

number_of_people = int(input("How many people to split the bill? "))

# calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# calculate the total bill
total_bill = total_bill + tip_amount

# calculate the bill per person
bill_per_person = total_bill / number_of_people

# display the bill per person
print(f"Each person should pay: £{bill_per_person:.2f}")

# display a goodbye message
print("Goodbye and Thank you!")
