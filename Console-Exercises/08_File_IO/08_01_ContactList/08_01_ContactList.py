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


def search_Contact(searched):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    found = False
    # for line in lines (and for every line i+1)
    for i, line in enumerate(lines):
        if searched in line: 

            start = i

            while start > 0 and "Name" not in lines[start]:
                start -= 1
            
            #print msg
            print(lines[start])
            print(lines[start+1])
            print(lines[start+2])
            print(lines[start+3])

            found = True
            break

    if not found:
        print(f"Contact '{searched}' was not found")


def show_Contacts():
    with open(file_path, 'r') as file:
        text = file.read()

    print(text)


def load_File(path):
    try:
        with open(path, 'r') as file_to_load:
            lines_to_load = file_to_load.read()

        with open(file_path, 'w') as file:
            file.write(lines_to_load)

        print(f"Loaded file from {path}")
    except FileNotFoundError:
        print(f"File '{path}' not found")


def handle_selection(selection):

    if selection == 1:
        print("-----Add Contact-----")
        contact_name = input("Enter Contact Name: ")
        contact_phone = input("Enter Contact Phone: ")
        contact_email = input("Enter Contact Email: ")

        add_Contact(contact_name, contact_phone, contact_email)

    elif selection == 2:
        print("-----Remove Contact-----")
        contact_to_remove = input("Enter name of contact to remove: ")
        remove_Contact(contact_to_remove)

    elif selection == 3:
        print("-----Search Contact-----")
        searched_contact = input("Search contact by Name, Email or Phone: ")
        search_Contact(searched_contact)

    elif selection == 4:
        print("-----Show All-----")
        show_Contacts()

    else:
        print("-----Load from File-----")
        load_file_path = input("Enter file path: ")
        load_File(load_file_path)

while True:
    try:
        selection = int(input("-----Select action-----\n" \
        "(1) add contact\n" \
        "(2) remove contact\n" \
        "(3) search contact\n" \
        "(4) show all\n" \
        "(5) load from file\n"))

        if selection in range(1,6):
            handle_selection(selection)
        else:
            print("Please enter a number in range of 1-5")

    except(ValueError):
        print("Please enter a valid number")