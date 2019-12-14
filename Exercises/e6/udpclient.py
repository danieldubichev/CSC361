
import socket

import sys

# Create a UDP socket
csocket = socket(AF_INET, SOCK_DGRAM)

server_address = ('', 8888)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print ( 'sending ' + message)
    csocket.sendto(message.encode(), server_address)

    # Receive response
    print ('waiting to receive')
    data, server = csocket.recvfrom(4096)
    print ("received " + data)

finally:
    print ("closing socket")
    csocket.close()
