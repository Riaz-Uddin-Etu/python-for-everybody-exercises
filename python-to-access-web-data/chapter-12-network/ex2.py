import socket

address = input('Provide the url: ')

try:
    parts = address.split('/')
    HOST = parts[2]
    PORT = 80

    # http protocols
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((HOST, PORT))
        
    command = f'GET {address} HTTP/1.0\r\n\r\n'.encode() # encode() - socket only transmit binary not string
    mysocket.send(command)

    counts = 0
    printable = 0
    limit = 3000

    while True:
        data = mysocket.recv(512)
        if len(data) < 1: break

        if printable < limit:
            remain = limit - printable
            piece = data[:remain]
            print(piece.decode(errors='replace'), end='')
            printable += len(piece)
        
        # Count the entire document
        counts += len(data)     

    print('\nTotal Count: ', counts)

    mysocket.close()

except:
    print('Provide a valid url (e.g,: http://www.example.com/page.html/document.txt)')


