import time             #for time library
from socket import *    #for udp
import sys              #args & error checking


#udp init
try:
    csocket = socket(AF_INET, SOCK_DGRAM)
except socket.error:
    print("Failed to create socket for UDP")
    sys.exit()
#cmd args

#ip address
ipaddy = str(sys.argv[1])

#port number
portnumber = int(sys.argv[2])

#informative print
print "Exchanging data with IP ADDRESS: "+ ipaddy+ ", and PORT NUMBER: " + str(portnumber)

#loop
firsttennums = range(1,11)

#data analysis
totalroundtimes = 0
times = []

for number in firsttennums:

    timesnapshot = time.time()
    timestring = time.strftime("%H:%M:%S")
    
    #message = ping sequenceNumber time
    

    message = "Ping " + str(number) + " " +  str(timestring) 
    csocket.sendto(message, (ipaddy, portnumber))
    
    #exception socket.timeout
    #This exception is raised when a timeout occurs on a socket which has had timeouts enabled via a prior call to settimeout().
    
    csocket.settimeout(1)

    try:
        received, clientAddress = csocket.recvfrom(1024)
        timetaken = (time.time() - timesnapshot)
	totalroundtimes += timetaken
        times.append(timetaken)
        print(received)
    except timeout:
        print("Request timed out")
	totalroundtimes += 1
        times.append(1)
        continue

print

for roundtimes in range(0,10):
    currenttime = str(times[roundtimes])
    print("RTT for PING " + str(roundtimes) + " " + currenttime)

print

averageroundtimes = str(totalroundtimes/10) 

print("The average round time for the 10 PING's was : " + averageroundtimes)

csocket.close()