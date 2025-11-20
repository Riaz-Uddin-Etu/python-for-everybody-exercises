# Parsing HTML by re
# Extracting links

import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Avoid SSL Certificate Errors
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# user prompt
address = input('Enter address: ')

wpage = urllib.request.urlopen(address, context=context).read()
links = re.findall(b'href="(http[s]?://.+?)"', wpage)
# convert list to string
for link in links:
    print(link.decode())