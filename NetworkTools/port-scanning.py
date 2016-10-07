# usr/bin/python27 Python 2.7
# importing nmap module
import nmap

# setting nm to nmap.PortScanner
nm = nmap.PortScanner()

# getting host from user
host = raw_input("Target: ")
# getting ports from user
ports = raw_input("Ports (ex. 22,13,42,144-928): ")
# getting arguments
arguments = raw_input('Arguments (Like your using regular NMAP): ')
# scanning
nm.scan(hosts=host, ports=ports, arguments=arguments)

# ----------------------------------------------------------------------------
# main menu
while True:
    print "WHAT WOULD YOU LIKE TO DO?"
    print \
        """
        [1] Get all hosts that were scanned
        [2] Get NMAP scan information
        [3] Get list of host-names
        [4] Get state of host
        [5] Get all scanned protocols
        [6] Get all ports for TCP
        [7] Get all ports for UDP
        [8] Get all ports for IP
        [9] Get all ports for SCTP
        [0] Quit
        """
    user_choice = int
    while (9 < user_choice) or (user_choice < 1):
        try:
            user_choice = int(raw_input(">>> "))
        except:
            print "Try again"
    # ----------------------------------------------------------------
    # choices
    if user_choice == 1:
        print nm.all_hosts()
    if user_choice == 2:
        print nm.scaninfo()
    if user_choice == 3:
        print nm[host].hostnames()
    if user_choice == 4:
        print nm[host].state()
    if user_choice == 5:
        print nm[host].all_protocols()
    if user_choice == 6:
        print nm[host].all_tcp()
    if user_choice == 7:
        print nm[host].all_udp()
    if user_choice == 8:
        print nm[host].all_ip()
    if user_choice == 9:
        for item in nm.all_hosts():
            print nm[nm.all_hosts().index(item)].all_sctp()
    if user_choice == 0:
        exit()