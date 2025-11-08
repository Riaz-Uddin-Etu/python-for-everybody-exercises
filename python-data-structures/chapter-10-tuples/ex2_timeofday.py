# Exercise 2:

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhand = open(fname, 'r')
except:
    print('Enter valid file.')
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    hour = line[5].split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1

for k, v in sorted(counts.items()):
    print(k,v)
