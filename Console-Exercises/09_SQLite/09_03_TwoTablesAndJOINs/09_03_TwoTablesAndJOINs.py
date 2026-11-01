import sqlite3
import os
import sys

library_path = os.path.join(os.path.dirname(__file__), "library3.db")
conn = sqlite3.connect(library_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        pages INTEGER,
        status TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(id)
    )
""")

authors = [
    ("George Orwell",),
    ("Frank Herbert",),
    ("J.R.R. Tolkien",),
    ("Isaac Asimov",),
    ("Ursula K. Le Guin",),
]
books = [
    ("1984", 1, 328, "finished"),
    ("Animal Farm", 1, 112, "reading"),
    ("Dune", 2, 412, "unread"),
    ("Dune Messiah", 2, 256, "unread"),
    ("Children of Dune", 2, 444, "unread"),
    ("The Hobbit", 3, 310, "finished"),
    ("Foundation", 4, 255, "unread"),
    ("I, Robot", 4, 253, "finished"),
]

cursor.execute("SELECT 1 FROM authors LIMIT 1")
if cursor.fetchone() is None:
    # executemany
    cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)
    # OR for loop
    #for name in authors:
    #    cursor.execute("INSERT INTO authors (name) VALUES (?)", name)
    cursor.executemany("INSERT INTO books (title, author_id, pages, status) VALUES (?, ?, ?, ?)", books)
    conn.commit()

def print_book(book):
    print(f"[{book['book_id']}] {book['title']} by {book['author_name']} - {book['pages']} pages ({book['status']})")

def print_total_books(row):
    print(f"{row['name']} - {row['total_books']} books")
    
def print_total_pages(row):
    print(f"{row['name']} - {row['total_pages']} pages")
    
def add_book(title, author_name, pages, status):
    cursor.execute("SELECT id FROM authors WHERE name = ?", (author_name,))
    author = cursor.fetchone()

    if author is None:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
        author_id = cursor.lastrowid
    else:
        author_id = author["id"]

    cursor.execute(
        "INSERT INTO books (title, author_id, pages, status) VALUES (?, ?, ?, ?)",
        (title, author_id, pages, status)
    )
    book_id = cursor.lastrowid
    conn.commit()

    book = {
        "book_id": book_id,
        "title": title,
        "author_name": author_name,
        "pages": pages,
        "status": status
    }

    print("Book added:")
    print_book(book)

def total_books_perAuthor():
    cursor.execute("""
        SELECT authors.name, COUNT(books.id) AS total_books
        FROM authors
        LEFT JOIN books ON books.author_id = authors.id
        GROUP BY authors.id
    """)
    rows = cursor.fetchall()

    if not rows:
        print("No books yet")
        return
    for row in rows:
        print_total_books(row)

def total_pages_perAuthor():
    cursor.execute("""
        SELECT authors.name, SUM(books.pages) AS total_pages
        FROM books
        JOIN authors ON books.author_id = authors.id
        GROUP BY authors.id
        ORDER BY total_pages DESC
    """)
    rows = cursor.fetchall()

    if not rows:
        print("No books yet")
        return
    for row in rows:
        print_total_pages(row)

def show_all():
    cursor.execute("""
        SELECT books.id AS book_id, books.title, authors.name AS author_name,
               books.pages, books.status
        FROM books
        JOIN authors ON books.author_id = authors.id
        ORDER BY books.title
    """)
    rows = cursor.fetchall()

    if not rows:
        print("No books yet")
        return
    for row in rows:
        print_book(row)
    

# Management
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
        print("-----Total Books per Author-----")
        total_books_perAuthor()

    elif selection == 3:
        print("-----Total Pages per Author-----")
        total_pages_perAuthor()

    elif selection == 4:
        print("-----Show all Books-----")
        show_all()

    elif selection == 5:
        print("-----Exit-----")
        conn.close()
        sys.exit()

    else:
        print("Invalid selection")

while True:
    try:
        selection = int(input("-----Select action-----\n"
                              "(1) Add Book\n"
                              "(2) Total books per Author\n"
                              "(3) Total pages per Author\n"
                              "(4) Show All\n"
                              "(5) Exit\n"))

        if selection in range(1, 6):
            handle_selection(selection)
        else:
            print("Please enter a number in range of 1-5")

    except ValueError:
        print("Please enter a valid number")