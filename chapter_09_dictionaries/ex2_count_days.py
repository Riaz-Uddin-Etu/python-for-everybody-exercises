fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    days = words[2]
    counts[days] = counts.get(days, 0) + 1
print(counts)