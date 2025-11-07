fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print(''' NA NA BOO BOO TO YOU - You have been punk'd! ''')
        exit()
    else:
        print(f'File cannot be opened: {fname}')
        exit()

count = 0
for line in fhand:
    if not line.startswith('Subject:'):
        continue
    count += 1
print(f'There were {count} subject lines in {fname}')