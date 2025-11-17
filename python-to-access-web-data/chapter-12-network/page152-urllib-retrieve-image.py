# Reading binary files using urllib
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()

fhand = open('cover3.jpg', 'wb') # write a file in storage
fhand.write(img) # write binary file (image) in cover3.jpg
fhand.close()
