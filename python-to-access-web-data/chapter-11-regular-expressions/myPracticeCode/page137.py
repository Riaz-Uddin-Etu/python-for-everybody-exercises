#But when you are using findall(), parentheses indicate that while you want the
#whole expression to match, you only are interested in extracting a portion of the
#substring that matches the regular expression.

import re

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.strip()
    x = re.findall('^X\\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

