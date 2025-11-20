# Reading binary files using urllib
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')

fhand = open('cover3.jpg', 'wb') # write a file in storage

size = 0
while True:
    data = img.read(100000)
    if len(data) < 1: break # guardian pattern
    size = size + len(data)
    # print(len(data), size)
    fhand.write(data)

print('Total downloaded: ', size)

fhand.close()
