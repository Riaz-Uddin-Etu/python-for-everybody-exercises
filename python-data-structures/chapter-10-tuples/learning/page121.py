# sort words by the length of word in descending

txt = 'but soft what light in yonder window breaks'
words = txt.split()
ls = list()
for word in words:
    ls.append((len(word), word)) # (len(word), word) ====> This is a tuple


ls.sort(reverse=True) # for descending --> (reverse=True) bcs default ascending
lsTwo = list()
for length, word in ls:
    lsTwo.append(word)

print(ls)
print(lsTwo) 

# Sort compares the first elemnt, if first elemnt is tie then go to second
# [(6, 'yonder'), (6, 'window'), (6, 'breaks')]