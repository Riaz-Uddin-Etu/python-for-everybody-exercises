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

    while True:
        data = mysocket.recv(1024)
        if len(data) < 1: break
        pos_2CRLF = data.find(b'\r\n\r\n') 
        data = data[pos_2CRLF+4:]
        print(data.decode(), end='')

    mysocket.close()

except:
    print('Provide a valid url (e.g,: https://www.example.com/page.html/document.txt)')


