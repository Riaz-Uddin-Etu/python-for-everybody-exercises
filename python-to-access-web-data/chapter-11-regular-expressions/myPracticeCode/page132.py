import re 

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)








# Similar code

# fhand = open('mbox-short.txt')

# for line in fhand:
#     line = line.strip()
#     if line.startswith('From:'):
#         print(line)