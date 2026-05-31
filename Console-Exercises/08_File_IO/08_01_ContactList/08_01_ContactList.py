import os
script_dir = os.path.dirname(__file__) # script_dir = direction of this file
file_path = os.path.join(script_dir, 'contacts.txt') # file_path is direction of this file(script_dir) + file (contacts.txt)


def add_Contact(name, phone, email):
    with open(file_path, 'a') as file:
        file.write(f"Name  : {name}\nPhone : {phone}\nEmail : {email}\n--------------------\n")
    print(f"Contact {name} added!")


def remove_Contact(name):
    with open(file_path, 'r') as file:
        lines = file.readlines() # lines is a list of all lines

    new_lines = []
    skip = 0
    
    for line in lines:
        if skip > 0:
            skip -= 1
            continue  # Skip line until contact is removed
        
        if f"Name  : {name}" in line:
            skip = 3  # Skip 3 lines
            continue
        
        new_lines.append(line)  # Safe rest of lines

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

    print(f"Contact {name} removed!")
            

def handle_selection(selection):

    if selection == 1:
        print("-----Add Contact-----")
        contact_name = input("Enter Contact Name: ")
        contact_phone = input("Enter Contact Phone: ")
        contact_email  = input("Enter Contact Email: ")

        add_Contact(contact_name, contact_phone, contact_email)

    elif selection == 2:
        print("-----Remove Contact-----")
        contact_to_remove = input("Enter name of contact to remove: ")
        remove_Contact(contact_to_remove)

    elif selection == 3:
        print("-----Search Contact-----")

    elif selection == 4:
        print("-----Show All-----")

    elif selection == 5:
        print("-----Save to File-----")

    else:
        print("-----Load from File-----")

while True:
    try:
        selection = int(input("-----Select action-----\n" \
        "(1) add contact\n" \
        "(2) remove contact\n" \
        "(3) search contact\n" \
        "(4) show all\n" \
        "(5) save to file\n" \
        "(6) load from file\n"))

        if selection in range(1,7):
            handle_selection(selection)
        else:
            print("Please enter a number in range of 1-6")

    except(ValueError):
        print("Please enter a valid number")