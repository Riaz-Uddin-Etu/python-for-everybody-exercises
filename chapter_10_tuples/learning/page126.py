# 10.7 Using tuples as keys in dictionaries
directory = dict()
last,first = ('riaz', 'etu')
number = '01869'
directory[last, first] = number

print(directory)

for k, v in directory:
    print(v, k, directory[last,first])
