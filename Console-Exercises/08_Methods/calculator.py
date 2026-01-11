print("=== Welcome to the Simple Calculator ===")

# =============================== MATH FUNCTIONS ===============================
# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "!!! Error! Division by zero. !!!"
    return a / b

# Root
def root(a, b):
    if a < 0:
        return "!!! Error! Cannot compute square root of negative number. !!!"
    return a ** (1 / b)

# Power
def power(a, b):
    return a ** b


# ============================== RESTART OR CLOSE ==============================

def restart_or_close():
    global mode

    #ask user to restart or close
    continue_calc = input("Do you want to perform another calculation? (y/n): ")

    #if yes, restart
    if continue_calc.lower() == 'y':
        mode = get_mode()
        InputLogic()
    
    #if no, close
    else:
        print("======= Calculator closed. ========")

#=============================== GET TWO NUMBERS ===============================

def get_two_numbers():
    #get two numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

#================================= INPUT LOGIC =================================
def InputLogic():
    if mode == 0:
        print("======= Calculator closed. ========")

    # Addition
    elif mode == 1:
        print("============ Addition =============")
        num1, num2 = get_two_numbers()
        answer = add(num1, num2)

    # Subtraction
    elif mode == 2:
        print("=========== Subtraction ===========")
        num1, num2 = get_two_numbers()
        answer = subtract(num1, num2)

    # Multiplication
    elif mode == 3:
        print("========= Multiplication ==========")
        num1, num2 = get_two_numbers()
        answer = multiply(num1, num2)

    # Division
    elif mode == 4:
        print("============ Division =============")
        num1, num2 = get_two_numbers()
        answer = divide(num1, num2)

    # Root
    elif mode == 5:
        print("============== Root ===============")
        num1, num2 = get_two_numbers()
        answer = root(num1, num2)

    # Power
    elif mode == 6:
        print("============== Power ==============")
        num1, num2 = get_two_numbers()
        answer = power(num1, num2)

    print(f"Result: {answer}")

    # Ask to restart or close
    restart_or_close()

# =============================== INPUT SECTION ================================

def get_mode():
    #Give user options
    print(
        "Choose mode: \n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Root\n"
        "6. Power\n"
        "0. Close"
    )
    #Get user input
    choice = input("Enter choice (1, 2, 3, 4, 5, 6) or 0 to close: ")
    return int(choice)

# ================================ MAIN PROGRAM ================================
mode = get_mode()
InputLogic()

# Section Banner
print("====================================")