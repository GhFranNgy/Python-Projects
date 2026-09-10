import sqlite3
import os

library_path = os.path.join(os.path.dirname(__file__), "library.db")
conn = sqlite3.connect(library_path)
cursor = conn.cursor()
books = []

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        pages INTEGER,
        status TEXT
    )
""")
for i in range(5):
    insert_book = {
        "title": input("Enter book title: "),
        "author": input("Enter book author: "),
        "pages": int(input("Enter number of pages: ")),
        "status": input("Enter book status: ")
    }
    books.append(insert_book)

cursor.executemany("""INSERT INTO books
    (title, author, pages, status) VALUES (?, ?, ?, ?)""", books)
conn.commit()
conn.close()