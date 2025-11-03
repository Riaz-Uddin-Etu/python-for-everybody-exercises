fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()
largest = None
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]  
    counts[email] = counts.get(email, 0) + 1 # Counting email -- Like Histogram

# Retrieving largest sender
for k in counts:
    if largest is None or counts[k] > largest:  # counts[k] == value
        l_sender = k
        largest = counts[k]

print(l_sender, largest)

