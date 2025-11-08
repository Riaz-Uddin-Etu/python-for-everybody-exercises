# Exercise 1:

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhand = open(fname, 'r')
except:
    print('Enter valid file.')
    exit()

commits_counts = dict()
for line in fhand:
    if not line.startswith('From '): continue
    line = line.rstrip()
    line = line.split()
    address = line[1]
    commits_counts[address] = commits_counts.get(address, 0) + 1

commits_ls = list()
for email, count in commits_counts.items():
    commits_ls.append((count, email))
commits_ls.sort(reverse=True)

# Most commits
count, email = commits_ls[0]
print(email, count)
