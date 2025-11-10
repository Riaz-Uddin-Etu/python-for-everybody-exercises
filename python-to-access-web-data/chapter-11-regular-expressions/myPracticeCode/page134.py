# extracting data using findall()

import re

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.strip()
    x = re.findall('[a-zA-Z0-9]\S*@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

