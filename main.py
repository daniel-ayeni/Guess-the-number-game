# to import random module
import random

# to create a range of random numbers between 1-100
n = random.randrange(1, 100)
while True:
    try:
        # to take a user input to enter a number
        guess = int(input("Enter any number: >_"))
        while n != guess:  # means if n is not equal to the input guess
            # if guess is smaller than n
            if guess < n:
                print("Too low")
                # to again ask for input
                guess = int(input("Enter number again: >_"))
            # if guess is greater than n
            elif guess > n:
                print("Too high!")
                # to again ask for the user input
                guess = int(input("Enter number again: >_"))
            # if guess gets equals to n terminate the while loop
            else:
                break
        print(str(n), "you guessed it right!!")
        break
    except ValueError:
        print("Enter a whole number")


