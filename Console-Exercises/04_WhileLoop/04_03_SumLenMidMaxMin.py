numbers = []
value_counter = 1
print("-1 to stop")

# get user input and fill numbers
while True:
    
    # check if input is a valid input
    try:
        user_input = int(input(f"Enter {value_counter} number: \n"))
    except ValueError:
        print("Error!!! That was not a number.")
        continue

    if user_input == -1:
        break

    numbers.append(user_input)
    value_counter+=1

#check if numbers is empty
if len(numbers) > 0:
    
    # print filled numbers
    print(f"All entered numbers {numbers}")

    # length of numbers
    print(f"Length of numbers is: {len(numbers)}")

    # sum all numbers values
    total = sum(numbers)
    print(f"Sum of all numbers values is: {total}")

    # arithmetic mean of numbers
    arithmetic_mean = total / len(numbers)
    print(f"Arithmetic mean of all numbers values is: {arithmetic_mean}")

    # maximum of numbers
    print(f"Maximum of numbers is: {max(numbers)}")

    # minimum of numbers
    print(f"Minimum of numbers is: {min(numbers)}")

# if numbers is empty
else:
    print("Error!!! No numbers were entered.")