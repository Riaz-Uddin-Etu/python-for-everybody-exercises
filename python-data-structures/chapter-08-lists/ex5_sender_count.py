#Exercise 5: Minimalist Email Client.

fname = input("Enter file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    line = line.strip()
    if not line.startswith('From '): continue
    words = line.split()
    sender = words[1]
    count += 1
    print(sender)

print(f'There were {count} lines in the file with From as the first word')
