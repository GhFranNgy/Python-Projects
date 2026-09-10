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

# 3. Select and print all books
print("--- All books ---")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

# 4. Select and print books where status = 'reading'
print("\n--- Currently reading ---")
cursor.execute("SELECT * FROM books WHERE status = ?", ("reading",))
for row in cursor.fetchall():
    print(row)

# 5. Select and print books sorted by pages descending
print("\n--- Sorted by pages (descending) ---")
cursor.execute("SELECT * FROM books ORDER BY pages DESC")
for row in cursor.fetchall():
    print(row)

conn.close()