import sqlite3
import os
import sys

library_path = os.path.join(os.path.dirname(__file__), "library2.db")
conn = sqlite3.connect(library_path)
conn.row_factory = sqlite3.Row
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


def print_book(row):
    print(f"[{row['id']}] {row['title']} by {row['author']} - {row['pages']} pages ({row['status']})")


def add_book(title, author, pages, status):
    cursor.execute(
        "INSERT INTO books (title, author, pages, status) VALUES (?, ?, ?, ?)",
        (title, author, pages, status)
    )
    conn.commit()
    print(f"Book '{title}' by {author} added.")


def update_status(book_id):
    new_status = input("Enter new status: ")
    cursor.execute("UPDATE books SET status = ? WHERE id = ?", (new_status, book_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("No book with that ID.")
    else:
        print("Status updated.")


def remove_book(title):
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    matches = cursor.fetchall()
    if not matches:
        print("Book not found.")
        return

    for row in matches:
        print_book(row)

    try:
        book_id = int(input("Enter ID to delete: "))
    except ValueError:
        print("Please enter a number")
        return

    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    if book is None:
        print("No book with that ID.")
        return

    confirm = input("Enter title to confirm deletion: ")
    if confirm == book["title"]:
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        print("Book deleted.")
    else:
        print("Title didn't match, deletion cancelled.")


def search_book(findbythis):
    print(f"\n--- Results for '{findbythis}' ---")
    pattern = f"%{findbythis}%"
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR status LIKE ?",
        (pattern, pattern, pattern)
    )
    results = cursor.fetchall()
    if not results:
        print("No books found.")
        return
    for row in results:
        print_book(row)


def show_all():
    print("\n--- Show all sorted by pages (descending) ---")
    cursor.execute("SELECT * FROM books ORDER BY pages DESC")
    rows = cursor.fetchall()
    if not rows:
        print("No books yet.")
        return
    for row in rows:
        print_book(row)


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
            book_id = int(input("ID: "))
        except ValueError:
            print("Please enter a number")
            return

        update_status(book_id)

    elif selection == 3:
        print("-----Remove Book-----")
        title = input("Title: ")

        remove_book(title)

    elif selection == 4:
        print("-----Search Book-----")
        book = input("Search book by Title/author/status: ")

        search_book(book)

    elif selection == 5:
        print("-----Show All-----")
        show_all()

    elif selection == 6:
        print("-----Exit-----")
        conn.close()
        sys.exit()

    else:
        print("Invalid selection")


while True:
    try:
        selection = int(input("-----Select action-----\n"
                              "(1) Add Book\n"
                              "(2) Update Status\n"
                              "(3) Remove Book\n"
                              "(4) Search Book\n"
                              "(5) Show All\n"
                              "(6) Exit\n"))

        if selection in range(1, 7):
            handle_selection(selection)
        else:
            print("Please enter a number in range of 1-6")

    except ValueError:
        print("Please enter a valid number")

#TODO
#Understand