import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur  = conn.cursor()

cur.executescript(''' 
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;                  

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
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

    cur.execute(''' INSERT OR IGNORE INTO Artist (name)
                    VALUES (?) ''', (artist, ))
    cur.execute(''' SELECT id FROM Artist WHERE name = ? ''', (artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO Album (title, artist_id) 
                    VALUES (?, ?)''', (album, artist_id))
    cur.execute(''' SELECT id FROM Album WHERE title = ?''', (album, ))
    album_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO Genre (name) 
                    VALUES (?)''', (genre, ))
    cur.execute(''' SELECT id FROM genre WHERE name = ? ''', (genre, ))
    genre_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) 
                    VALUES (?, ?, ?, ?, ?, ?)''', (track_name, album_id, genre_id, length, rating, count))
    
    
conn.commit()

cur.close()
