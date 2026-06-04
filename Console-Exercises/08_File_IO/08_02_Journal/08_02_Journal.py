import os

script_dir = os.path.dirname(__file__)
journal_folder = os.path.join(script_dir, "journal_data")

os.makedirs(journal_folder, exist_ok=True)

file_list = []
file_list_path = []

def load_existing_entries():
    if os.path.exists(journal_folder):
        for filename in os.listdir(journal_folder):
            if filename.endswith('.txt'):
                file_list.append(filename.replace('.txt', ''))
                file_list_path.append(os.path.join(journal_folder, filename))

def write_entry(date, title, content):
    file_path = os.path.join(journal_folder, f"{date}.txt")

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{title}\n{content}\n")
    if date not in file_list:
        file_list.append(date)
        file_list_path.append(file_path)

def read_journal():
    for i in range(len(file_list)):
        with open(file_list_path[i], "r", encoding="utf-8") as file:
            entry = file.read()

        print(file_list[i])
        print(entry)

def search_entry(date):
    for i in range(len(file_list_path)):
        if date in file_list_path[i]:
            with open(file_list_path[i], "r", encoding="utf-8") as file:
                entry = file.read()

            print(f"\n{file_list[i]}")
            print(entry)
            
def delete_entry(date):
    search_entry(date)
    confirmed = input("To delete confirm with \"yes\": \n")

    if confirmed == "yes":
        for i in range(len(file_list_path)):
            if date in file_list_path[i]:
                os.remove(file_list_path[i])

    else: print("Abort delete. Delete was not confirmed")

def handle_selection(selection):

    if selection == 1:
        print("-----Write Entry-----")
        entry_Date = input("Date: ")
        entry_Title = input("Title: ")
        entry_Text = input("Text:\n")
        
        write_entry(entry_Date, entry_Title, entry_Text)

    elif selection == 2:
        print("-----Read Journal-----")
        read_journal()

    elif selection == 3:
        print("-----Search Entry-----")
        search_Date = input("Enter search date: ")
        search_entry(search_Date)

    else:
        print("-----Delete Entry-----")
        delete_Date = input("Date of entry to delete: ")
        delete_entry(delete_Date)

# main 
load_existing_entries()
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