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

#================================= INPUT LOGIC =================================

"""def InputLogic():
    if mode == 0:
        print("======== Calculator closed. ========")

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

    return answer"""

# Section Banner
#print("====================================")