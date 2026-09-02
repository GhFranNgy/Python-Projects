import os
import json
import sys

script_dir = os.path.dirname(__file__)
inventory_path = os.path.join(script_dir, "inventory.json")

inventory = []

def load_inventory(inventory):
    print("Load Inventory...")
    try:
        with open(inventory_path, "r") as f:
            items = json.load(f)

    except FileNotFoundError:
        print(f"Error: {inventory_path} nicht gefunden.")
        sys.exit()

    except json.JSONDecodeError:
        print("Missing or damaged file.")
        sys.exit()

    for item in items:
        inventory.append(item)

    print("Done.")


def save_inventory(items):
    print("Save Inventory...")
    with open(inventory_path, "w") as f:
        json.dump(items, f, indent=2)
    print("Done.")

def get_next_id(inventory):
    if not inventory:
        return 1
    return max(item["id"] for item in inventory) + 1 # pulls out largest ID and adds 1


def add_item(inventory, name, quantity, price):
    try:
        quantity = int(quantity)
        price = float(price)

    except ValueError:
        print("Quantity must be a whole number and price must be a number.")
        return
    
    for item in inventory:
        if item["name"] == name:
            existing_item = item
            break

    if existing_item:
        existing_item["quantity"] += quantity
    else:
        item = {
            "id": get_next_id(inventory),
            "name": name,
            "quantity": quantity,
            "price": price
        }
        inventory.append(item)

    save_inventory(inventory)
    print(f"Added {name} (id={item['id']}, {quantity} @ {price}).")

def remove_item(inventory, name, quantity):
    try:
        if quantity != "all":
            quantity = int(quantity)
    except ValueError:
        print("Quantity must be a whole number or \"all\" ")
        return
    for item in inventory:
        if item["name"] == name:
            if quantity == "all":
                item["quantity"] = 0
                print(f"Removed {name} (id={item['id']}, 0 @ 0).")
            else: 
                if item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    print(f"Removed {name} (id={item['id']}, {item["quantity"]} @ {item["price"]}).")
                else:
                    print(f"There are only {item["quantity"]} in stock")
    else:
        print("Name not found")

    save_inventory(inventory)


def update_price(inventory, name, price):

def find_low_stock(inventory, treshold):

def handle_selection(selection):

    if selection == 1:
        print("-----Add item-----")
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price:")
        
        add_item(inventory, name, quantity, price)

    elif selection == 2:
        print("-----remove item-----")
        name = input("Name: ")
        quantity = input("Quantity: ")

        remove_item(inventory, name, quantity)

    elif selection == 3:
        print("-----Update price-----")
        name = input("Name: ")
        new_price = input("Price:")

        update_price(inventory, name, new_price)

    else:
        print("-----Find low stock-----")
        threshold = input("Threshold: ")

        find_low_stock(inventory, threshold)


load_inventory(inventory)
save_inventory(inventory)

# main
while True:
    try:
        selection = int(input("-----Select action-----\n" \
            "(1) Write\n" \
            "(2) Read\n" \
            "(3) Search\n" \
            "(4) Delete\n"))

        if selection in range(1,5):
            handle_selection(selection)
        else:
            print("Please enter a number in range of 1-4")

    except(ValueError):
        print("Please enter a valid number")