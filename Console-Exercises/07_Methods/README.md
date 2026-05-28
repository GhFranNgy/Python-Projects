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

07_03_TodoList
* Initialize empty todo dictionary
* Define functions
  - add_task(task) → set status to False and store in dictionary
  - remove_task(task) → delete task if exists, else print error
  - mark_done(task) → set status to True if exists, else print error
  - show_all() → loop through all tasks and display with status
  - show_pending() → loop through tasks and show only False (not done)
* Get action selection
  - Display menu (1-5)
  - Loop until valid input (1-5)
  - Handle ValueError for invalid input
* Process action
  - Action 1 → get task name and call add_task()
  - Action 2 → get task name and call remove_task()
  - Action 3 → get task name and call mark_done()
  - Action 4 → call show_all()
  - Action 5 → call show_pending()
* Main loop
  - Get action selection
  - Process based on selection
  - Continue until user exits

07_04_TemperatureConverter
* Initialize empty history dictionary and counter
* Define conversion functions
  - get_Fahrenheit(celsius) → calculate (c × 9/5) + 32 and store in history
  - get_Celsius(fahrenheit) → calculate (f - 32) × 5/9 and store in history
  - get_Kelvin(celsius) → calculate c + 273.15 and store in history
* Store conversion in history
  - store_in_history(temp, converted, method) → use global counter as key
  - Add tuple to history dictionary
  - Increment counter
* Manage history
  - show_history() → loop through history and print all conversions
  - clear_history() → delete all history
* Get action selection
  - Display menu (1-5)
  - Loop until valid input (1-5)
  - Handle ValueError for invalid input
* Process action
  - Action 1 → get celsius and convert to fahrenheit
  - Action 2 → get fahrenheit and convert to celsius
  - Action 3 → get celsius and convert to kelvin
  - Action 4 → call show_history()
  - Action 5 → call clear_history()
* Main loop
  - Get action selection
  - Process based on selection
  - Continue until user exits

  07_05_BankAccount
* Create BankAccount class with __init__(name, balance)
  - Initialize name, balance, empty transaction list
* Define methods
  - deposit(amount) → check if positive, add to balance, store transaction, return balance or False
  - withdraw(amount) → check if positive and sufficient funds, subtract from balance, store transaction, return balance or False
  - get_Balance() → return current balance
  - get_Transactions() → loop through transactions and print each
* Authentication
  - Prompt for name and password
  - If valid → create account and continue
  - If invalid → deny access
* Get action selection
  - Display menu (1-4)
  - Loop until valid input (1-4)
  - Handle ValueError
* Process action
  - Action 1 → get amount and deposit, check return value
  - Action 2 → get amount and withdraw, check return value
  - Action 3 → show balance
  - Action 4 → show all transactions
* Main program
  - Authenticate user
  - Create account object
  - Loop for continuous operations