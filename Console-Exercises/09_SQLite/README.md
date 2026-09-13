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