import pprint

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
    at = email.find('@') # find position of @
    name = email[:at] # Slcie name 
    counts[name] = counts.get(name, 0) + 1 # Counting email -- Histogram
pprint.pprint(counts)
