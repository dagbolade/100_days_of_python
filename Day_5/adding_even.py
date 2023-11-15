# adding even numbers with uaer input
target = int(input("Enter a number: "))
total = 0
for number in range(2, target + 1, 2):
    total += number
print(total)

# or

alt_total = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alt_total += number
print(alt_total)