import random

print("Random Number Guess Game")
num = random.randint(1, 100)
guess = int(input("Pick a number beween 1 and 100\n"))
tries = 1

while guess != num:
    if guess > num:
        guess = int(input("Your Number is bigger than my number, guess again\n"))
    else:
        guess = int(input("Your Number is smaller than my number, guess again\n"))
    tries += 1

print(f"You guessed it on your {tries} try")