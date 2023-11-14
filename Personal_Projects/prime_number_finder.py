# Prime Number Finder

number = int(input("Enter a number to check if it is a prime number: "))
prime = True
for num in range(2, number):
    if number % num == 0:
        prime = False
if prime:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
