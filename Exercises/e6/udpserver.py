import socket
import sys

# Create a UDP socket
serversocket = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the port
serversocket.bind(('', 8888))
print ("starting up on localhost port 8888")

while True:
    print ('waiting to receive message')
    message, address = serversocket.recvfrom(4096)
    
    print (" received " + len(message) + " bytes from" + address)
    print (" message is : " + message)
    
    if message:
        sent = serversocket.sendto(message, address)
        print (" sent " + sent + " bytes back to " + address)
