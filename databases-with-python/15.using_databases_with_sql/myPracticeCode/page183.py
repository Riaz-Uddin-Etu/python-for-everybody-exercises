import sqlite3

conn = sqlite3.connect('library.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books')
cur.execute('CREATE TABLE books (title TEXT, quantity INTEGER)')

cur.close()