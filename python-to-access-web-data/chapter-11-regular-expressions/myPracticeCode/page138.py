# From this:
# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
# Find the last digits

import re

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.strip()
    numbers = re.findall('^Details: .+rev=([0-9]+)', line)
    if len(numbers) > 0:
        print(numbers)