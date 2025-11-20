import urllib.request
from bs4 import BeautifulSoup
import ssl

# ignore ssl certificate
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


address = input('Enter url: ')
wpage = urllib.request.urlopen(address, context = context).read()
soup = BeautifulSoup(wpage, 'html.parser')

anchors = soup('a') # Give a list of anchor tag string 

print('TAG: ', anchors)

# List to string
# get() is a beautifulsoup method, which retrieve the value of attribute of html tag
# Thus we get value of attribute href of html <a> tag
for anchor in anchors:
    print('TAG: ', anchor)
    print('URL: ', anchor.get('href', None)) 
    # if len(anchor.contents) < 1: continue
    if anchor.contents: print('CONTENTS: ', anchor.contents[0]) # guardian pattern to check the empty list
    print('ATTRIBUTES: ', anchor.attrs, '\n')


