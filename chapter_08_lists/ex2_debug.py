# Exercise 2:

fhand = open('debug_text_file.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2:
        continue
    if words[0] != 'From:':
        continue
    email = words[1]
    count += 1
    print(email)
print('Total:', count)