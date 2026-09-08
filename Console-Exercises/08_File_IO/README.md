# 08_FILE_IO

This folder contains exercises on reading and writing files.

================================================================================

08_01_ContactList
* Set up file path
  - Use os.path to get script directory and create contacts.txt path
* Define contact functions
  - add_Contact(name, phone, email) → append to file
  - remove_Contact(name) → read all lines, skip contact + 3 lines, write back
  - search_Contact(searched) → find in any line, work backward to find start, print contact block
  - show_Contacts() → read and display entire file
  - load_File(path) → copy external file to contacts.txt with error handling
* Remove contact logic
  - Read all lines into list
  - Use skip counter to skip matched contact + next 3 lines
  - Write remaining lines back to file
* Search contact logic
  - Use enumerate to track line position
  - Find searched term in any line
  - Work backward to find "Name" line
  - Print 4-line contact block
* Load from file
  - Prompt for file path
  - Read external file and copy to contacts.txt
  - Handle FileNotFoundError
* Get action selection
  - Display menu (1-5)
  - Loop until valid input (1-5)
  - Handle ValueError
* Process action
  - Action 1 → add contact
  - Action 2 → remove contact
  - Action 3 → search contact
  - Action 4 → show all contacts
  - Action 5 → load from file
* Main loop
  - Get selection and process
  - Continue until exit

08_02_Journal
* Set up folder structure
  - Create journal_data folder in script directory with os.makedirs()
  - Initialize file_list and file_list_path to track entries
* Load existing entries
  - On startup, loop through journal_data folder
  - Find all .txt files and add to tracking lists
* Define journal functions
  - write_entry(date, title, content) → create {date}.txt file with content
  - read_journal() → loop through all entries and display
  - search_entry(date) → find and display specific entry
  - delete_entry(date) → confirm with user, remove file with os.remove()
* Entry format
  - Each entry is separate file: YYYY-MM-DD.txt
  - Contains: title line, content line
  - Use encoding='utf-8' for special characters
* Get action selection
  - Display menu (1-4)
  - Handle ValueError
* Process action
  - Action 1 → write new entry
  - Action 2 → read all entries
  - Action 3 → search entry by date
  - Action 4 → delete entry by date
* Main loop
  - Get selection and process
  - Continue until exit

08_03_ServerLog
* Set up file paths
  - Use os.path to get script directory and create paths for server.log, info.txt, error.txt, warning.txt
* Initialize counters
  - info_counter, error_counter, warning_counter as global variables, starting at 0
* Define read_file()
  - Declare counters as global to modify them inside the function
  - Open server.log and read all lines
  - Loop through lines, check for "INFO", "ERROR", "WARNING"
  - Increment matching counter and pass line to corresponding write function
* Define write functions
  - add_info_Msg(line) → append line to info.txt
  - add_err_Msg(line) → append line to error.txt
  - add_warn_Msg(line) → append line to warning.txt
  - All use "a" mode so lines accumulate instead of overwriting
* Define output()
  - Print final counts for errors, infos, warnings
* Main flow
  - Call read_file() then output()

08_04_GradeBook
* Set up file paths
  - Use os.path to get script directory and create paths for grades.csv, report.csv
* Initialize tracking lists
  - grades → holds raw rows read from CSV
  - valid_grades → holds rows that passed validation and have an Average
* Define read_file()
  - Open grades.csv with csv.DictReader
  - Append each row to grades list
  - Handle FileNotFoundError, quit() if file missing
* Define get_average(grades)
  - For each row, get subject keys (all except "Name")
  - Convert subject values to int, catch ValueError for invalid entries
  - Skip row on ValueError, print warning
  - Calculate average = sum(values) / len(values), rounded to 2 decimals
  - Add "Average" key to row, append to valid_grades
* Define sort_after_average(grades)
  - Bubble sort: nested loops compare neighboring rows
  - Swap if left row's Average is smaller than right row's (descending order)
* Define create_report(grades)
  - Use csv.DictWriter with fixed fieldnames (Name, Math, English, Science, Average)
  - Write header and all rows to report.csv
* Define best_and_last(grades)
  - Best student = first row after sorting (highest average)
  - Last student = last row after sorting (lowest average)
* Define class_average(grades)
  - Average of all "Average" values across all students
* Measure runtime
  - Use time.perf_counter() before and after main flow
  - Print total runtime at the end
* Main flow
  - read_file() → get_average() → sort_after_average() → create_report() → best_and_last() → class_average()

08_05_JSONInventoryManager
* Set up file paths
  - Use os.path to get script directory and create inventory.json path
* Load/save inventory
  - load_inventory(inventory) → read JSON, handle FileNotFoundError and JSONDecodeError with sys.exit()
  - save_inventory(items) → write JSON with json.dump(), indent=2
* Define get_next_id(inventory)
  - Return 1 if inventory is empty
  - Otherwise find max existing id and add 1
* Define add_item(inventory, name, quantity, price)
  - Convert quantity/price to int/float, catch ValueError
  - Check if item with same name exists → add to quantity instead of duplicating
  - Otherwise create new item dict with id, name, quantity, price
  - Save inventory after change
* Define remove_item(inventory, name, quantity)
  - Accept quantity as number or "all"
  - Find item by name, reduce or zero out quantity
  - Handle insufficient stock and item-not-found cases
  - Save inventory after change
* Define update_price(inventory, name, price)
  - Find item by name, convert price to float, catch ValueError
  - Update price, save inventory
* Define find_low_stock(inventory, threshold)
  - Loop through inventory, print items where quantity < threshold
* Define handle_selection(selection)
  - Route menu choice to add/remove/update_price/find_low_stock
  - Prompt for required inputs via input()
* Main loop
  - Load and save inventory once at start
  - Display menu, validate input with try/except ValueError
  - Loop until program exit

08_06_LibraryTracker (Capstone)
* Set up file paths
  - library.json (source of truth), export.csv (generated report), reading_log.txt (append-only action log)
* Load/save library
  - load_library(library) → read JSON, handle FileNotFoundError/JSONDecodeError, log load action, return loaded list
  - save_library(library) → write JSON, log save action
* Define get_next_id(library)
  - Same max-id-plus-one pattern as inventory task
* Define add_book(library, title, author, pages, status)
  - for...else duplicate check (title + author match)
  - Convert pages to int, catch ValueError
  - Build book dict with id, append, save, log
* Define update_status(library, title)
  - Find book by title, confirm author with user (handles duplicate titles)
  - Numbered menu for status selection (Reading/Finished/Not Started) instead of free text
  - break after handling match, for...else prints "not found"
  - Log status change
* Define remove_book(library, title)
  - Collect all title matches, show them, confirm correct book
  - Select by id, require typing exact title to confirm deletion
  - library.remove(book), save, log removal
* Define search_book(library, title)
  - Collect and print all title matches
  - Log search action
* Define show_stats(library)
  - Total books, total pages via sum()
  - Count books per status (Reading/Finished/Not Started) via manual loop
  - Print full book list
  - Log stats action
* Define export_csv(library)
  - Sort books by pages descending using sorted() with key=lambda
  - Write to export.csv with csv.DictWriter, fixed fieldnames
* Define handle_selection(selection)
  - Routes menu choice 1-7 to add/update/remove/search/stats/export/exit
* Main loop
  - Load library once at start
  - Display menu, validate input with try/except ValueError
  - Loop until exit