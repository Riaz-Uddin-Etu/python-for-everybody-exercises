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
    email = words[1]  
    counts[email] = counts.get(email, 0) + 1 # Counting email -- Like Histogram

# Retrieving largest sender
lrg_word = None
lrg_count = None

for word, count in counts.items():
    if lrg_count is None or count > lrg_count:
        lrg_word = word
        lrg_count = count

print(lrg_word, lrg_count)
