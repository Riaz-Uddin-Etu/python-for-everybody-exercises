# Using urllib, we can treat a web page much like a file. 
# We simply indicate which web page we would like to retrieve 
# urllib handles all of the HTTP protocol and header details.

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    line = line.decode().strip().split()
    for word in line:
        counts[word] = counts.get(word, 0) + 1

print(counts)
