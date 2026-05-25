history = {}
history_counter = 0

def get_Fahrenheit(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    print(f"{Celsius:.2f}°C convert to {Fahrenheit:.2f}°F")

    store_in_history(Celsius, Fahrenheit, "Celsius to Fahrenheit")

def get_Celsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5/9
    print(f"{Fahrenheit:.2f}°F convert to {Celsius:.2f}°C")

    store_in_history(Fahrenheit, Celsius, "Fahrenheit to Celsius")

def get_Kelvin(Celsius):
    Kelvin = Celsius + 273.15
    print(f"{Celsius:.2f}°C convert to {Kelvin:.2f}°K")

    store_in_history(Celsius, Kelvin, "Celsius to Kelvin")

def show_history():
    for convertion in history:
        print(history[convertion])

def clear_history():
    history.clear()
    print("Cleared History")

def store_in_history(temp_to_convert, converted_temp, convert_method):
    global history_counter
    history[history_counter] = temp_to_convert, converted_temp, convert_method
    history_counter +=1

def handle_selection(selection):
    if selection == 1:
        print("-----Convert to Fahrenheit-----")
        temp_to_convert = float(input("Enter in °C: "))
        get_Fahrenheit(temp_to_convert)

    elif selection == 2:
        print("-----Convert to Celsius-----")
        temp_to_convert = float(input("Enter in °F: "))
        get_Celsius(temp_to_convert)

    elif selection == 3:
        print("-----Convert to Kelvin-----")
        temp_to_convert = float(input("Enter in °C: "))
        get_Kelvin(temp_to_convert)

    elif selection == 4:
        print("-----Show History-----")
        show_history()

    else:
        print("-----Clear History-----")
        clear_history()

while True:
    try:
        selection = int(input("-----Select action-----\n" \
        "(1) Celsius → Fahrenheit\n" \
        "(2) Fahrenheit → Celsius\n" \
        "(3) Celsius → Kelvin\n" \
        "(4) Show history\n" \
        "(5) Clear history\n"))

        if selection in range(1,6):
            handle_selection(selection)
        else:
            print("Please enter a number in range of 1-5")

    except(ValueError):
        print("Please enter a valid number")