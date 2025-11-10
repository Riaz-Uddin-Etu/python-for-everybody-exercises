# Using period (.), asterisk (*), and add (+) to match the strings
import re

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.strip()
    if re.search('^From:.+@', line):
        print(line)

