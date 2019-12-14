from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
# Change these values 
mailserver = ["smtp.uvic.ca", 25]

# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket("AF_INET", "SOCK_STREAM")
mailUrl = mailserver[0]
portNum = mailserver[1]
clientSocket.connect(mailserver[0], mailserver[1])


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Danny\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
#??????
mailFromCommand = "mail from: danieldubichev@uvic.ca\r\n"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
#??????
rcptToCommand = "rcpt to: danieldubichev@uvic.ca\r\n"
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')


# Send DATA command and print server response. 
#??????
dataCommand = "data\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
#??????
clientSocket.send(msg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Message ends with a single period.
#???????
clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')


# Send QUIT command and get server response.
smtpquit =  "quit\r\n"
clientSocket.send(smtpquit.encode())
recv7 = clientSocket.recv(1024).decode()
if recv7[:3] != '221':
    print('221 reply not received from the server')

