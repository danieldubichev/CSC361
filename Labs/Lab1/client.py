from socket import *

import sys

#type "python client.py 128.338.251.26 6789 hello.html"
# 	                   argv[1]    argv[2]  argv[3]


IP_address = sys.argv[1]
Port_number = sys.argv[2]
File_name = sys.argv[3]

#address = "%s:%s" %(IP,Port)

print(IP_address)
print(Port_number)
print (File_name)

#Establish Connect client socket
try:

	Client_socket = socket(AF_INET,SOCK_STREAM)

	Client_socket.connect((IP_address, int(Port_number)))

	Headerfrfr = "GET /%s HTTP/1.1" %(File_name)

	Client_socket.send("%s\r\n\r\n" %(Headerfrfr))


#error handling
except IOError:

	sys.exit(1)


#receive data back from the server
#includes header line

stringbuffer = ""

receiving = Client_socket.recv(4096)

while receiving:

	stringbuffer += receiving

	receiving = Client_socket.recv(4096)



Client_socket.close()



print ("String:", stringbuffer)
