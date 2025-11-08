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
    email = words[1]  # Retrieve eamil from list words
    pos_at = email.find('@')
    domain = email[pos_at + 1 : ] # Slicing the domain name
    counts[domain] = counts.get(domain, 0) + 1 # Counting email -- Histogram
print(counts)

