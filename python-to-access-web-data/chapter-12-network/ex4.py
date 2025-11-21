from bs4 import BeautifulSoup
import urllib.request
import ssl

# ignore ssl cert.
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Parsing the html text
address = input('Enter url: ')
wtext = urllib.request.urlopen(address, context=context).read()
soup = BeautifulSoup(wtext, 'html.parser')

paragraph = soup('p')

print(len(paragraph))

