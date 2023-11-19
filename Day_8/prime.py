def prime_checker(number):
    prime = True
    # check if number is less than 100
    if number < 100:
        # check if number is prime
        for num in range(2, number):
            if number % num == 0:
                prime = False
            else:
                prime = True
        if prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")

    else:
        print("Enter a number less than 100")


n = int(input("Check this number: "))
prime_checker(number=n)
