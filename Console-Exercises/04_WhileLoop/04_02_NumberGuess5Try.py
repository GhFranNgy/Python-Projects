import random

print("Random Number Guess Game")
num = random.randint(1, 100)

# First guess
guess = int(input("Pick a number between 1 and 100\n"))
tries = 1
maxTries = 5

# While tries is not maxTries yet
while tries < maxTries:

    # if guess is num then win
    if guess == num:
        print(f"You guessed it on your {tries} try ({num})")
        break

    # wrong guess and hints
    if guess > num:
        guess = int(input("Your Number is bigger than my number, guess again\n"))
    else:
        guess = int(input("Your Number is smaller than my number, guess again\n"))
    
    # adding tries
    tries += 1

# If Tries == maxTries & guess != num
else:
    print(
        "You took more than 5 guesses,\n"
        f"The number was {num}\n"
        "!!!You lost!!!"
    )