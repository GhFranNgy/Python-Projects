# 09_SQL

This folder contains exercises on SQL and SQLite, following the file I/O unit.

================================================================================

09_01_BooksTable
* Set up database connection
  - Use os.path to get script directory and create library.db path
  - Connect with sqlite3.connect(), create a cursor
* Create table
  - CREATE TABLE IF NOT EXISTS books (id, title, author, pages, status)
  - id as INTEGER PRIMARY KEY AUTOINCREMENT, replaces manual get_next_id() from Python tasks
  - title/author as TEXT NOT NULL, pages as INTEGER, status as TEXT
* Collect book input
  - Loop 5 times, prompt for title, author, pages (int), status
  - Build each as a dict, append to books list
* Insert into database
  - cursor.executemany() with parameterized query
  - Known issue: executemany() needs tuples matching (?, ?, ?, ?) positionally — a list of dicts fails
  - Fix: either use named placeholders (:title, :author, :pages, :status) matching dict keys, or convert dicts to tuples first
  - conn.commit() required after INSERT to persist changes
* Query the data
  - SELECT * FROM books → print all rows via cursor.fetchall()
  - SELECT * FROM books WHERE status = ? → filtered query with parameter tuple
  - SELECT * FROM books ORDER BY pages DESC → sorted query
  - Rows returned as plain tuples (no column names), unlike Python's DictReader
* Close connection
  - conn.close() at the end

Tooling
* SQLite = the database engine (via Python's built-in sqlite3 module, no install needed)
* SQL = the query language itself, not a specific program
* MySQL = server-based database, needed once multiple users/programs access the same data concurrently — the problem JSON files can't solve
* SQLit (Microsoft Store) = chosen GUI client to inspect library.db visually — SQL editor, results grid, object explorer for tables/indexes/foreign keys, works offline

09_02_BooksTable2
* Set up database
  - Use os.path to get script directory and create library2.db path
  - Connect with sqlite3.connect(), set conn.row_factory = sqlite3.Row before creating the cursor
  - CREATE TABLE IF NOT EXISTS books (id, title, author, pages, status)
* Define print_book(row)
  - Print one book using column names (row['title'] etc.)
* Define add_book(title, author, pages, status)
  - INSERT with parameterized query (?, ?, ?, ?), commit
* Define update_status(book_id)
  - UPDATE books SET status = ? WHERE id = ?, commit
  - Check cursor.rowcount, 0 means no book with that id
* Define remove_book(title)
  - SELECT matches by title with cursor.execute() + fetchall(), print them
  - Ask for ID, convert to int, return on ValueError
  - SELECT by id with fetchone(), None means not found
  - Require typing the title to confirm, then DELETE by id and commit
* Define search_book(findbythis)
  - One query: WHERE title LIKE ? OR author LIKE ? OR status LIKE ?
  - Pattern built as %term% for partial matches
* Define show_all()
  - SELECT * ORDER BY pages DESC, handle empty table
* Define handle_selection(selection)
  - Route menu choice 1-6 to add/update/remove/search/show all/exit
  - Input validated with try/except ValueError, return on bad input
  - Exit closes the connection with conn.close() before sys.exit()
* Main loop
  - Connection opened once at start, reused for the whole session
* Lessons
  - The cursor that runs the query must be the one you fetch from
  - Single-element tuples need a trailing comma: (book_id,)
  - fetchall() returns a list, fetchone() returns one row or None
  - DELETE/UPDATE on a missing id fails silently, so check rowcount or SELECT first

09_03_BooksAuthors
* Set up database
  - library3.db via os.path, conn.row_factory = sqlite3.Row before creating the cursor
  - PRAGMA foreign_keys = ON (SQLite doesn't enforce foreign keys by default)
* Create tables
  - authors (id, name TEXT NOT NULL UNIQUE)
  - books (id, title, author_id, pages, status, FOREIGN KEY author_id REFERENCES authors(id))
  - Author is stored once, each book points to it by number
* Seed data
  - Lists of tuples for authors and books, inserted with executemany
  - Only runs when authors is empty (SELECT 1 FROM authors LIMIT 1, fetchone() is None)
  - One author (Le Guin) has no books on purpose, to show JOIN vs LEFT JOIN
* Define print helpers
  - print_book(book) → book_id, title, author_name, pages, status
  - print_total_books(row) → name, total_books
  - print_total_pages(row) → name, total_pages
  - Each helper reads the column names (AS aliases) of its own query
* Define add_book(title, author_name, pages, status)
  - SELECT id FROM authors WHERE name = ? and fetchone()
  - Author missing → INSERT author, author_id = cursor.lastrowid
  - Author exists → author_id = author["id"]
  - INSERT book with author_id, book_id = cursor.lastrowid
  - One commit for author and book together
  - Build dict with the keys print_book expects, print it
* Define total_books_perAuthor()
  - FROM authors LEFT JOIN books ON books.author_id = authors.id GROUP BY authors.id
  - COUNT(books.id) AS total_books, authors without books get 0
* Define total_pages_perAuthor()
  - JOIN books with authors, GROUP BY authors.id
  - SUM(books.pages) AS total_pages, ORDER BY total_pages DESC
  - Plain JOIN leaves out authors without books
* Define show_all()
  - JOIN books with authors, aliases book_id and author_name, ORDER BY books.title
* Define handle_selection(selection)
  - Route menu choice 1-5 to add book / books per author / pages per author / show all / exit
  - Bad pages input retried in a loop with try/except ValueError
  - Exit closes the connection with conn.close() before sys.exit()
* Main loop
  - Menu validated with try/except ValueError and range(1, 6)
* Concepts
  - JOIN ... ON = matching rule that pairs each book with its author row
  - LEFT JOIN keeps every row of the left table, the missing side is NULL
  - GROUP BY = one pile per value, the aggregate (COUNT, SUM) works inside each pile
  - Aggregates skip NULL: COUNT(*) counts rows, COUNT(column) counts non-NULL values
  - Clause order: SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY
  - cursor.lastrowid only changes after an INSERT
  - AS aliases in the query must match the keys the print helper reads
  - A foreign key checks that the author exists, not that it is the right one