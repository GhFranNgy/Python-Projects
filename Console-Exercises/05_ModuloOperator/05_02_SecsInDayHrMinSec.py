import colorama
colorama.init(autoreset=True)

while True:
    try:
        time = int(input("Enter seconds to convert: \n"))

        if time < 0:
            print(colorama.Fore.RED + "Seconds cannot be negative.")
            continue
        break

    except ValueError:
        print(
            colorama.Fore.RED + "!!!Error!!! \n"
            "That was not a valid number."
        )

days = time // 86400
remaining = time % 86400

hours = remaining // 3600
remaining = remaining % 3600

minutes = remaining // 60
remaining = remaining % 60

seconds = remaining

print(
    f"{time} Seconds equal "
    f"{days} Days "
    f"{hours} Hours "
    f"{minutes} Minutes and "
    f"{seconds} Seconds"
)
