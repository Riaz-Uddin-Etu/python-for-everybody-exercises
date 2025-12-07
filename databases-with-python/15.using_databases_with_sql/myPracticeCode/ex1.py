# Task: We will read all the eamils from a text files 
# Then store the emails in a database using SQL
# And count them (emails) and will store in DB

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS email_counts')

cur.execute('CREATE TABLE email_counts (email TEXT, count INTEGER)')

file = input('Enter the file name: ')
if len(file) < 1: file = 'mbox-short.txt'
fhand = open(file)

for line in fhand:
    line = line.strip()
    if not line.startswith('From '): continue
    line = line.split()
    if len(line) < 1: continue
    emails = line[1]
    cur.execute(''' SELECT count FROM email_counts 
                    WHERE email = ? ''', (emails,))
    row = cur.fetchone() # It gives one row as tuple if there are no more rows, it returns None.
    if row is None:
        cur.execute(''' INSERT INTO email_counts (email, count) 
                        VALUES (?, 1) ''', (emails,))
    else:
        cur.execute(''' UPDATE email_counts SET count = count + 1 
                        WHERE email = ? ''', (emails,))
    
conn.commit()

# Retrieve Data to see
sqldata = cur.execute(''' SELECT email, count FROM email_counts ORDER BY count DESC''')

for row in sqldata:
    print(row[0], row[1])
    
    

