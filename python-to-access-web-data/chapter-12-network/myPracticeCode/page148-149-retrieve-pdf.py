import socket

HOST = 'do1.dr-chuck.com'
PORT = 80 # which is the default port for HTTP.
link = 'https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf'

# creates a TCP socket.
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((HOST, PORT))

# Sends a raw HTTP GET request asking the server for pythonlearn.pdf.
# HTTP/1.0 is the HTTP version used
# \r\n\r\n marks blank line in the end of the headers.
# .encode() converts the string to bytes, since sockets transmit bytes, not strings.
resource = f'GET {link} HTTP/1.0\r\n\r\n'.encode()
mysocket.send(resource)
count = 0
pdf_files = b'' # bytes object

while True:
    # reads up to 5120 bytes from the server.
    data = mysocket.recv(5120) # returns a chunk of image as bytes
    if len(data) < 1: break
    count = count + len(data)
    print(len(data), 'Total receive: ', count)
    # To reconstruct the entire pdf, you need to combine all these chunks into a single bytes object.
    pdf_files = pdf_files + data

mysocket.close()

# Look for the end of the header (2 CRLF)
pos = pdf_files.find(b'\r\n\r\n') #gives 2crlf index position
print('Header length: ', pos)
print('type of pdf_files: ', type(pdf_files))
print('\n', pdf_files[:pos].decode()) # gives only the header bytes. decode header bytes to string

# Removing the header, keeping only pdf bytes
picture = pdf_files[pos+4:] # \r\n\r\n is 4 bytes long

# Saving the binary pdf
fhand = open('stuff.pdf', 'wb')
fhand.write(pdf_files)
fhand.close()


# <headers end here>\r\n\r\n<binary pdf data starts>