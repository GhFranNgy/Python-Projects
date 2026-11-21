import sqlite3
import os
import sys
import time

database_path = os.path.join(os.path.dirname(__file__), '09_04_QueryWorkonBigDatabase_Shop.db')
conn = sqlite3.connect(database_path)
cursor = conn.cursor

