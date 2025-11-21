import urllib.request
import ssl

address = input('Provide the url: ')

# Ignore the ssl 
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


try:
    parts = address.split('/')
    
    wtext = urllib.request.urlopen(address, context=context)

    counts = 0
    printable = 0
    limit = 3000
    count2 = 0

    while True:
        data = wtext.read(1024)
        if len(data) < 1: break

        if printable < limit:
            remain = limit - printable
            piece = data[:remain]
            print(piece.decode(errors='replace'), end='')
            printable += len(piece)
        
        # Count the entire document
        counts += len(data)     

    print('\nTotal Count: ', counts, 'printable: ', printable)

except:
    print('Provide a valid url (e.g,: http://www.example.com/page.html/document.txt)')


