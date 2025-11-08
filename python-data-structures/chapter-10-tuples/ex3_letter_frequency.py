# Exercise 3

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'ex3_sample.txt'

try:
    fhand = open(fname)
except:
    print('Enter valid file.')
    exit()

counts = dict()
for line in fhand:
    line = line.strip()
    for letter in line:
        letter = letter.lower()
        if 'a' <= letter <= 'z':
            counts[letter] = counts.get(letter, 0) + 1

# prints the letters in decreasing order of frequency.
# Used List Comprehensions instead of four line for loop
ls = sorted([(frequency, letter) for letter, frequency in counts.items()], reverse=True)

for frequency, letter in ls:
    print(frequency, letter)