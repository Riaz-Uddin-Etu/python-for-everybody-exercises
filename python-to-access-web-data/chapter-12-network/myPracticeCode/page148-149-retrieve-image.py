import socket
import time

HOST = 'data.pr4e.org'
PORT = 80 # which is the default port for HTTP.

# creates a TCP socket.
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((HOST, PORT))

# Sends a raw HTTP GET request asking the server for cover3.jpg.
# HTTP/1.0 is the HTTP version used
# \r\n\r\n marks blank line in the end of the headers.
# .encode() converts the string to bytes, since sockets transmit bytes, not strings.
resource = 'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode()
mysocket.sendall(resource)
count = 0
picture = b'' # bytes object

while True:
    # reads up to 5120 bytes from the server.
    data = mysocket.recv(5120) # returns a chunk of image as bytes in each call
    if len(data) < 1: break
    time.sleep(.50) # to grt rid of buffer take quarter seconds after receiving data - in the mean time data will be sent
    count = count + len(data)
    print(len(data), 'Total receive: ', count)
    # To reconstruct the entire image, you need to combine all these chunks into a single bytes object.
    picture = picture + data

mysocket.close()

print('type of picture: ', type(picture))

# Look for the end of the header (2 CRLF)
pos = picture.find(b'\r\n\r\n') #gives 2crlf index position
print('Header length: ', pos)
print('\n', picture[:pos].decode()) # gives only the header bytes. decode header bytes to string

# Removing the header, keeping only image bytes
picture = picture[pos+4:] # \r\n\r\n is 4 bytes long

# Saving the binary image
fhand = open('python.jpg', 'wb')
fhand.write(picture)
fhand.close()


# <headers end here>\r\n\r\n<binary image data starts>

