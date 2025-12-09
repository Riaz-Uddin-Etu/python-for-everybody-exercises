# Task: We will read all the eamil domains from a text file
# Then store the domains in a database using SQL
# And count them (domains) and will store in DB

import sqlite3

conn = sqlite3.connect('email_count_db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file = input('Enter the file name: ')
if len(file) < 1: file = 'mbox.txt'
fhand = open(file)

for line in fhand:
    line = line.strip()
    if not line.startswith('From '): continue
    line = line.split()
    if len(line) < 1: continue
    emails = line[1].split('@')[1]
    cur.execute(''' SELECT count FROM Counts 
                    WHERE org = ? ''', (emails,))
    row = cur.fetchone() # It gives one row as tuple if there are no more rows, it returns None.
    if row is None:
        cur.execute(''' INSERT INTO Counts (org, count) 
                        VALUES (?, 1) ''', (emails,))
    else:
        cur.execute(''' UPDATE Counts SET count = count + 1 
                        WHERE org = ? ''', (emails,))
    
conn.commit()

# Retrieve Data to see
sqldata = cur.execute(''' SELECT org, count FROM Counts ORDER BY count DESC''')

for row in sqldata:
    print(row[0], row[1])
    
    

