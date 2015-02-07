

#Client code for UDP Pinger
__author__ = 'Bhaumik'

from socket import *
import time

server = '127.0.0.1'
port = 12000
seq = 1


clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = raw_input("please Try to Test Server Response\n")
for i in range(10):

    starttime = (time.time())
    print 'This is starting time for' + " " + 'ping' + " " + str(seq) + " = " + str(starttime)
    seq = seq + 1

    clientSocket.sendto(message, (server, port))

    try:
        updatemessage, address = clientSocket.recvfrom(4096)

        updatemessage = updatemessage.split(',')
        end_time = (time.time())
        RTT = (end_time - starttime)
        print 'Round Time' + " " + str(RTT)
        print 'End Time' + " " + str(end_time) + "\n"

    except timeout:
        print 'It is timeout' + "\n"

