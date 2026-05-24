# 07_METHODS

This folder contains exercises on the use of methods.

================================================================================

07_01_SimpleCalculator
* Display welcome message
  - Print calculator banner
* Define math functions
  - Addition → return sum of two numbers
  - Subtraction → return difference
  - Multiplication → return product
  - Division
    - If divisor is 0 → return error message
    - Else return quotient
  - Root
    - If number is negative → return error message
    - Else compute a^(1/b)
  - Power → return a raised to b
* Get calculation mode
  - Display menu options (1–6, 0 to close)
  - Loop until valid input
    - Try converting input to integer
    - If out of range → ask again
    - If invalid → handle error
* Get two numbers
  - Prompt user for first number
  - Prompt user for second number
  - Convert inputs to float
  - Return both values
* Process input logic
  - If mode = 0 → close calculator
  - If mode = 1 → perform addition
  - If mode = 2 → perform subtraction
  - If mode = 3 → perform multiplication
  - If mode = 4 → perform division
  - If mode = 5 → perform root
  - If mode = 6 → perform power
  - Print result
* Restart or close
  - Ask user if they want another calculation
  - If “y” → get new mode and restart logic
  - Else → print closing message
* Main program execution
  - Call mode selection
  - Call input logic
  - Print closing separator

07_02_ShoppingCart
* Initialize empty basket dictionary
* Define functions
  - add_item(name, amount, price) → calculate total and store in basket
  - remove_item(name) → delete item if exists, else print error
  - total() → sum all prices and print with 2 decimals
  - items_count() → print length of basket
  - show_cart() → loop through basket and display all items
* Get shopping action
  - Display menu (1-5)
  - Loop until valid input (1-5)
  - Handle ValueError for invalid input
* Process action
  - Action 1 → get item details and call add_item()
  - Action 2 → get item name and call remove_item()
  - Action 3 → call total()
  - Action 4 → call items_count()
  - Action 5 → call show_cart()
* Main loop
  - Get action selection
  - Process based on selection
  - Continue until user exits