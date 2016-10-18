#!usr/bin/python

import socket                       # Importing socket module

s = socket.socket()                 # Create a socket object

connections = []                    # Creating a list of connections made or were possible
buffer_size = 20                    # setting buffer size

# setting up current machine connection information
host = socket.gethostname()         # Get local machine name
port = 1604                         # Reserve a port for your service
s.bind((host, port))                  # Binding to the port

print "Awaiting connection. Once connection is made, attack will start to comprimise system and show its vulnerabilities. Please only use this legally."
s.listen(5)                            # Listening for incomming connections
c, addr = s.accept()            # Accepts waiting connection
while True:
    data = c.recv(buffersize=buffer_size)
    if not data:
        break

    print "Recieved Data: ", data
c.close()


