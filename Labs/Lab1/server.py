#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
?????????????????

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  ??????????????? 
            
    try:
        message = ?????????????????               
        filename = message.split()[1]                 
        f = open(filename[1:]) 

        outputdata = ???????????????                  
        #Send one HTTP header line into socket
        ?????????????

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        ????????????

        #Close client socket
        ????????????

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
