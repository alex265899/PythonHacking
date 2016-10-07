#!usr/bin/python

import socket                       # Importing socket module

s = socket.socket()                 # Create a socket object

connections = []                    # Creating a list of connections made or were possible

while True:
    num_of_connections = raw_input("Maximum number of connections allowed?: ")      #Getting the maximum number of connections allowed by the user
    try:
        connection_number = int(num_of_connections)        # Try to convert to integer
        break                                               # Exit the loop
    except:
        "Please try again. Number only."                    # Asks the user for a proper input if any error are present

# setting up current machine connection information
host = socket.gethostname()         # Get local machine name
port = 1604                         # Reserve a port for your service
s.bind((host, port))                  # Binding to the port

for _ in range(0, int(connection_number)):
    s.listen                         # Listening for incomming connections
socket.socket.
    while True:
        c, addr = s.accept()            # Accepts waiting connection
        peer_address = s.getpeername()  # Getting peer information
        print 'Got connection from {0}'.format(addr)
        connections.append(peer_address)
        c.close()

print connections
