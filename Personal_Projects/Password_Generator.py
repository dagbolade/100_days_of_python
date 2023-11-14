# Password Generator
# easy level
import random
import string

print("Welcome to the PyPassword Generator!")
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
password = []
user_letters = int(input("How many letters would you like in your password? "))
user_numbers = int(input("How many numbers would you like in your password? "))
user_symbols = int(input("How many symbols would you like in your password? "))

for char in range(1, user_letters + 1):
    password.append(random.choice(letters))
for num in range(1, user_numbers + 1):
    password.append(random.choice(numbers))
for sym in range(1, user_symbols + 1):
    password.append(random.choice(symbols))
random.shuffle(password)
print("".join(password))

# hard level
import random
import string

print("Welcome to the PyPassword Generator 2!")
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

password = []
user_letters = int(input("How many letters would you like in your password? "))
user_numbers = int(input("How many numbers would you like in your password? "))
user_symbols = int(input("How many symbols would you like in your password? "))
user_password = ""

for char in range(1, user_letters + 1):
    password.append(random.choice(letters))
for num in range(1, user_numbers + 1):
    password.append(random.choice(numbers))
for sym in range(1, user_symbols + 1):
    password.append(random.choice(symbols))
random.shuffle(password)
for char in password:
    user_password += char
print(user_password)
