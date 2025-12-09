import json
import sqlite3

conn = sqlite3.connect('roasterdb.sqlite')
cur  = conn.cursor()

cur.executescript( '''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
                  
    CREATE TABLE User (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT UNIQUE
    );
    CREATE TABLE Course (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        title TEXT UNIQUE
    );
    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id)
    );
                  
''')


file_json = input('Enter file json name: ')
if len(file_json) == 0:
    file_json = 'roster_data.json'

file_handle = open(file_json, 'r').read()

json_data = json.loads(file_handle)

for item in json_data:
    name = item[0]
    course_title = item[1]
    role = item[2]
    
    cur.execute(''' INSERT OR IGNORE INTO User (name)
                    VALUES (?) ''', (name, ))
    cur.execute(''' SELECT id FROM User WHERE name = ? ''', (name,))
    user_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO Course (title)
                    VALUES (?) ''', (course_title,))
    cur.execute(''' SELECT id FROM Course WHERE title = ? ''', (course_title,))
    course_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR REPLACE INTO Member (user_id, course_id, role)
                    VALUES (?, ?, ?) ''', (user_id, course_id, role))
conn.commit()

# query = cur.execute(''' SELECT * FROM Member LIMIT 10;''')    
# for row in query:
#     print(row)

