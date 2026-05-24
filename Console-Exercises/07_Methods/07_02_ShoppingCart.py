basket = {}

def add_item(name, amount, price):
    price = amount * price
    basket[name] = price
    print(f"Added {name} for {price}€")
    
def remove_item(name):
    if name in basket:
        del basket[name]
        print(f"Removed {name} from basket")
    else:
        print(f"{name} was not found")

def total():#        .values == values of items in dict
    cost = sum(basket.values())
    print(f"Total: {cost:.2f}€")

def items_count():
    count = len(basket)
    print(f"There are {count} items in the basket.")

def show_cart():
    if basket:
        for item,price in basket.items():
            print(item,price)

def selected(selection):
    #1
    if selection == 1:

        print("-----Add to basket-----\n")
        item_to_add = input("Name of item to add: ")
        amount_to_add = int(input(f"Amount of {item_to_add}: "))
        price_of_item = float(input(f"Price of {item_to_add}: "))

        add_item(item_to_add, amount_to_add, price_of_item)

    #2
    elif selection == 2:

        print("-----Remove from basket-----\n")
        item_to_remove = input("Name of item to remove: ")

        remove_item(item_to_remove)

    #3
    elif selection == 3:

        print("-----Total cost-----")
        total()

    #4
    elif selection == 4:

        print("-----Cout of items-----")
        items_count()

    #5
    else:

        print("-----Show cart-----")
        show_cart()
        
while True:
    try:
        selection = int(input("-----Select action-----\n" \
        "(1) add to basket\n" \
        "(2) remove from basket\n" \
        "(3) show total cost\n" \
        "(4) show count of items in basket\n" \
        "(5) show basket\n"))

        if selection in range(1,6):
            selected(selection)
        
        print("Please enter a number in range of 1-5")

    except(ValueError):
        print("Please enter a valid number")