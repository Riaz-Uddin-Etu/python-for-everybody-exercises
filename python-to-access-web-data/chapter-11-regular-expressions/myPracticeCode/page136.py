# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000
# we don’t just want any floating-point numbers from any lines.
# We only want to extract numbers from lines that have the above syntax.

import re

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.strip()
    if re.search('^X\\S*: [0-9.]+', line):
        print(line)