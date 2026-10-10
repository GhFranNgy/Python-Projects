import sqlite3
import os
import sys

library_path = os.path.join(os.path.dirname(__file__), "library2.db")
conn = sqlite3.connect(library_path)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        pages INTEGER,
        status TEXT
    )
""")

def add_book(title, author, pages, status):
    conn.executemany("""INSERT INTO books
    (title, author, pages, status) VALUES (?, ?, ?, ?)""", [(title, author, pages, status)])
    conn.commit()

def update_status(id):
    # 2. Update status of book where id = id
    new_status = input("Enter new status: ")
    cur = conn.execute("UPDATE books SET status = ? WHERE id = ?", (new_status, id))
    conn.commit()
    if cur.rowcount == 0:
        print("No book with that ID.")
    
def remove_book(title):
    # 3. Delete book where title = title
    conn.execute("SELECT * FROM books WHERE title = ?", (title,))
    matches = cursor.fetchall()
    for row in matches:
        print(row)
    try:
        selectID = int(input("Enter ID to delete"))
    except ValueError:
        print("Please enter a number")
        return
    cur = cursor.execute("DELETE FROM books WHERE id = ?", (selectID,))
    conn.commit()
    if cur.rowcount == 0:
        print("No book with that ID.")

def search_status(status):
    # 4. Select and print books where status = status
    print("\n--- Books with status '{}' ---".format(status))
    cursor.execute("SELECT * FROM books WHERE status = ? COLLATE NOCASE", (status,))
    for row in cursor.fetchall():
        print(row)

def show_stats():
    # 5. Select and print books sorted by pages descending
    print("\n--- Sorted by pages (descending) ---")
    cursor.execute("SELECT * FROM books ORDER BY pages DESC")
    for row in cursor.fetchall():
        print(row)
    

def handle_selection(selection):

    if selection == 1:
        print("-----Add Book-----")

        title = input("Enter book title: ")
        author = input("Enter book author: ")
        while True:
            try:
                pages = int(input("Enter number of pages: "))
                break
            except ValueError:
                print("Please enter a valid number")

        insert_book = {
        "title": title,
        "author": author,
        "pages": pages,
        }

        add_book(insert_book["title"], insert_book["author"], insert_book["pages"], "Not Started")

    elif selection == 2:
        print("-----Update Status-----")
        try:
            id = int(input("ID: "))
        except ValueError:
            print("Please enter a number")
            return

        update_status(id)

    elif selection == 3:
        print("-----Remove Book-----")
        title = input("Title: ")

        remove_book(title)

    elif selection == 4:
        print("-----Search Status-----")
        status = input("Status: ")

        search_status(status)

    elif selection == 5:
        print("-----Show Stats-----")
        show_stats()

    elif selection == 6:
        print("-----Exit-----")
        conn.close()
        sys.exit()

    else:
        print("Invalid selection")

while True:
    try:
        selection = int(input("-----Select action-----\n" \
            "(1) Add Book\n" \
            "(2) Update Status\n" \
            "(3) Remove Book\n" \
            "(4) Search Book\n" \
            "(5) Show Stats\n" \
            "(6) Exit\n"))

        if selection in range(1,7):
            handle_selection(selection)
        else:
            print("Please enter a number in range of 1-6")

    except(ValueError):
        print("Please enter a valid number")