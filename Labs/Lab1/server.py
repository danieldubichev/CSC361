#import socket module
#to execute in mininet type "python server.py"
# "The server is ready to receive" immediately after
#open another terminal.
#type "python client.py 128.338.251.26 6789 hello.html"
#or go to firefox and type in http://localhost:6789/hello.html" and you should reveice the quoted message from line 3
from socket import *
import sys # In order to terminate the program

try:
	serverSocket = socket(AF_INET, SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit()
	
print 'Socket Created'
#Prepare a server socket

### Trying to get my servers real address when potentially 
### Several network interfaces are open. 
### Example : 
#
#				serversocket.bind((socket.gethostname(), 8089)) 
#
#Doing this we get our local host name then ask DNS what it thinks IP is.
#Problem is DNS may not know what your server name is or your server may have a different DNS name



	
serverSocket.bind(('', 6789)) 
print 'Socket now binded'

serverSocket.listen(10) #A queue of ten requests maximum
print 'Socket now listening'

while True:
    #Establish the connection
    print('Ready to serve...')
    #connectionSocket, addr =  ??????????????? 
    (connectionSocket, addr) = serverSocket.accept()
    print "Received connection from: ", addr 
	 
    try:
	
        message = connectionSocket.recv(1024)
	filename = message.split()[1]
	print "Message: ", message
        f = open(filename[1:]) 
        outputdata = f.read()             
        print "Data content: ", outputdata

	#Send one HTTP header line into socket

	connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
		
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        


        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        print 'IO Error'
	
	connectionSocket.send('HTTP/1.1 404 Not Found')

        #Close client socket
       
	connectionSocket.close()
		
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
