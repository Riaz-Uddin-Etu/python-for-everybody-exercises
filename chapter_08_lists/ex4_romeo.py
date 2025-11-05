# Exercise 4: Find all unique words in a file

fname = input("Enter file name: ")
fhand = open(fname)
unique_words = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

# Sort the unique list
unique_words.sort()
print(unique_words)

fhand.close()

