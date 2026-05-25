#Todo
# give user selection
# method to handle selection
# dict for todo list items
# method for adding task
# method for removing task
# method to check task
# method to show list
# method to show unchecked only

Todo_list = {}

def add_Task(task):
    Todo_list[task] = False
    print(f"Task added: {task}")

def remove_Task(task):
    if task in Todo_list:
        del Todo_list[task]
        print(f"Task removed: {task}")
    else:
        print(f"Task not found.")

def mark_done(task):
    if task in Todo_list:
        Todo_list[task] = True
        print(f"Task marked done: {task}")
    else:
        print(f"Task not found.")

def show_list():
    for task in Todo_list:
        status = "Done" if Todo_list[task] else "Not Done"
        print(f"{task}: {status}\n")

def show_pending():
    for task in Todo_list:
        if Todo_list[task] == False:
            status = "Done" if Todo_list[task] else "Not Done"
            print(f"{task}: {status}\n")

def selected(selection):
    #1
    if selection == 1:
        print("-----Add Task-----")
        pointer = input("Enter Task: ")
        add_Task(pointer)
    #2
    elif selection == 2:
        print("-----Remove Task-----")
        pointer = input("Task to Remove: ")
        remove_Task(pointer)
    #3
    elif selection == 3:
        print("-----Mark Done-----")
        pointer = input("Task to mark done: ")
        mark_done(pointer)
    #4
    elif selection == 4:
        print("-----Show All-----")
        show_list()
    #5
    else:
        print("-----Show Pending-----") 
        show_pending()

while True:
    try:
        selection = int(input("-----Select action-----\n" \
        "(1) add task\n" \
        "(2) remove task\n" \
        "(3) mark done\n" \
        "(4) show all\n" \
        "(5) show pending only\n"))

        if selection in range(1,6):
            selected(selection)
        else:
            print("Please enter a number in range of 1-5")

    except(ValueError):
        print("Please enter a valid number")