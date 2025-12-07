import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.execute(''' DROP TABLE IF EXISTS track ''')
cur.execute(''' CREATE TABLE track (title TEXT, plays INTEGER, artist_id INTEGER) ''')

cur.execute(''' INSERT INTO track (title, plays, artist_id) 
                VALUES ('My Way', 15, 42) ''')
cur.execute(''' INSERT INTO Track (title, plays, artist_id)
                VALUES ('New York', 25, 42) ''')
conn.commit()


cur.execute(''' DROP TABLE IF EXISTS artist ''')
cur.execute(''' CREATE TABLE artist (id INTEGER, name TEXT, eye TEXT) ''')

cur.execute(''' INSERT INTO artist (id, name, eye) 
                VALUES (42, 'Frank Sinatra', 'blue') ''')
conn.commit()


cur.execute('''SELECT title, plays, name, eye FROM track JOIN artist 
                       ON track.artist_id = artist.id ''')

for row in cur:
    print(row)

cur.close()