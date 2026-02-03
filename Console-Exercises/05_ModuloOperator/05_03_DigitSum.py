import colorama
colorama.init(autoreset=True)

digit_sum = 0

while True:

    try:
        num = int(input("Enter a number:\n"))
        num = abs(num)
        break
    except ValueError:
        print(colorama.Fore.RED + "No valid input try again")

while num > 0: 
    digit_sum += num % 10
    num //= 10    

print("Digit sum:", digit_sum)