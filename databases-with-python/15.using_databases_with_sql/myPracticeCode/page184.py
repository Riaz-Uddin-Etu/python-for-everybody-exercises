import sqlite3

conn = sqlite3.connect('library.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO books (title, quantity) VALUES(?,?)', ('Salat Jene Bujhe Porun', 10))
cur.execute('INSERT INTO books (title, quantity) VALUES(?,?)',('Stat for DS', 3))

conn.commit()
print('table: books')
cur.execute('SELECT title, quantity FROM books')
for row in cur:
    print(row)

cur.execute('DELETE FROM books WHERE quantity > 50')
conn.commit()

cur.close()