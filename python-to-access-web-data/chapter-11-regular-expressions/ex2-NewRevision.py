# Exercise 2:
import re
fname = input('Enter file: ')
fhand = open(fname)

numList =[]
for line in fhand:
    line = line.strip()
    number = re.findall('^New Revision: ([0-9]+)', line)
    
    # Make a list of all numbers
    if len(number) > 0:
        for i in number:
            numList.append(int(i))
            
average = int(sum(numList)/len(numList))
print(average)
