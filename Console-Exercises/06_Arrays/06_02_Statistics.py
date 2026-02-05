import random
import colorama
colorama.init(autoreset=True)

counter = [0] * 6
row_length = 10

dice_colors = {
    1: colorama.Back.LIGHTBLACK_EX,
    2: colorama.Back.LIGHTWHITE_EX,
    3: colorama.Back.LIGHTGREEN_EX,
    4: colorama.Back.LIGHTBLUE_EX,
    5: colorama.Back.LIGHTYELLOW_EX,
    6: colorama.Back.LIGHTMAGENTA_EX,
}

while True:
    try:
        throw_amount = int(input("Enter the amount of throws: \n"))
        if throw_amount <= 0:
            print(colorama.Fore.RED + "Number must be positive")
            continue
        break

    except ValueError:
        print(colorama.Fore.RED + "Invalid input, enter a number")

# print index of columns
print(colorama.Fore.BLUE + "  1 2 3 4 5 6 7 8 9 10")
# Print index of first line
print(colorama.Fore.BLUE + "0", end=" ")

for i in range(throw_amount):

    result = random.randint(1, 6)
    counter[result - 1] += 1

    # Print index of lines for new rows
    if i != 0 and i % row_length == 0:

        print()
        print(colorama.Fore.BLUE + f"{i // row_length}", end=" ")

    print(dice_colors[result] + f"{result}", end=" ")

# result
print("\n=========================")
for i in range(1, 7):
    print(f"{i} was thrown {counter[i-1]} times")
print("=========================")
