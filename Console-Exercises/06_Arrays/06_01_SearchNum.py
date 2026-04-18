import colorama
colorama.init(autoreset = True)

arr = [None] * 20
places_searched_num = []
counter_searched_num = 0

for i in range(len(arr)):

    while True:

        try:
            arr[i] = int(input(f"Enter your digit {i + 1}: "))
            break

        except ValueError:
            print(colorama.Fore.RED + "Invalid input! Please enter a number.")

print(colorama.Fore.GREEN + f"Your array is: {arr}")

while True:

    try:
        searched_num = int(input("Enter the seached number: "))
        break

    except ValueError:
        print(colorama.Fore.RED + "Invalid input! Please enter a number.")

for i in range(len(arr)):

    if arr[i] == searched_num:
        places_searched_num.append(i)
        counter_searched_num += 1

print(f"The searched Number appears {counter_searched_num} times at the places {places_searched_num + 1} of your list")
