# time of day of each mail message
# extract the hour of the day for each line.

import re

file = open('mbox-short.txt')

for line in file:
    line = line.strip()
    hour = re.findall('^From .+ ([0-9][0-9]):', line)
    if len(hour) > 0:
        print(hour)
    