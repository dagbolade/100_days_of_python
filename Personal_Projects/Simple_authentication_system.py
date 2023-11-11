# Simple authentication system Set up a dictionary called users which should contain at least 3 users,
# each user should have a minimum of 2 keys: 'username' and 'password' Ask the user to enter their username and
# password.
# check if their username and password exist in the dictionary
# if it does, print "You are now logged in"
# if not, print "Invalid username or password"

users = {'David': 'pass', 'user': 'pin', 'tracey': 'password'}
username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users.keys() and password in users.values():
    print("You are now logged in")
else:
    print("Invalid username or password")

