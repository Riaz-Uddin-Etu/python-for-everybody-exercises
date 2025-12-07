import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur  = conn.cursor()

cur.executescript(''' 
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS track;
                
CREATE TABLE artist ( id INTEGER PRIMARY KEY, name TEXT UNIQUE);           
CREATE TABLE album ( id INTEGER PRIMARY KEY, title TEXT UNIQUE, artist_id INTEGER);
CREATE TABLE genre ( id INTEGER PRIMARY KEY, genre TEXT UNIQUE);
CREATE TABLE track ( id INTEGER PRIMARY KEY, title TEXT UNIQUE, album_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)
''' )

conn.commit()

handle = open('tracks.csv')

for line in handle:
    line = line.strip()
    line = line.split(',')
    if len(line) != 7: continue
    
    track_name = line[0]
    artist = line[1]
    album = line[2]
    count = line[3]
    rating = line[4]
    length = line[5]
    genre = line[6]

    # print(track_name, artist, album, count, rating, length, genre)

    cur.execute(''' INSERT OR IGNORE INTO artist (name)
                    VALUES (?) ''', (artist, ))
    cur.execute(''' SELECT id FROM artist WHERE name = ? ''', (artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO album (title, artist_id) 
                    VALUES (?, ?)''', (album, artist_id))
    cur.execute(''' SELECT id FROM album WHERE title = ?''', (album, ))
    album_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO track (title, album_id, len, rating, count) 
                    VALUES (?, ?, ?, ?, ?)''', (track_name, album_id, length, rating, count))
    
    
conn.commit()

cur.close()
