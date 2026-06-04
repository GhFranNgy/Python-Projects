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