# Ten most common words
import string
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'romeo-full.txt'

fhand = open(fname, 'r')

d = dict()
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split() 
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
           
ls = list()
for k, v in d.items(): # items() gives list of tuples as key value pairs from dict.
    ls.append((v, k))

ls.sort(reverse=True)

for v, k in ls[:10]:
    print(k, v)