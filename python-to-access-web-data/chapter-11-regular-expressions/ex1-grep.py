import re
usrinp = input('Enter a regular expression: ')

fname = 'mbox.txt'
fhand = open(fname)

count = 0
for line in fhand:
    line = line.strip()
    match = re.findall(usrinp, line)
    if len(match) > 0:
        print(match)
        count += 1
print(f'{fname} had {count} lines that match {usrinp}')