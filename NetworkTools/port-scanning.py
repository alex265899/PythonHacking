#!usr/bin/env python3

# pylint: disable=C0103

# importing nmap module
import nmap

# creating object nm
nmscan = nmap.PortScanner()

# creating function called pscan for handling main port scan
def pscan(target, port, args):
    """
    This is the main function for running the port scan
    :param target: String containing the website or ip address
    :param port: String containing the ports to scan (ex. 22,33,44-55)
    :return: boolean
    """
    target = str(target)
    port = str(port)
    try:
        nmscan.scan(target, port, args)
        return True
    except BaseException:
        return False

# getting the target
addr = input('Target: ')
# getting the ports
ports = input('Ports: ')
# getting the arguments
arg = input('Arguments: ')

# initiating scan
pscan(addr, ports, args=arg)

# creating object stats and info
stats = nmscan.scanstats()
info = nmscan.scaninfo()
xml = nmscan.analyse_nmap_xml_scan()

# printing out scan statistics
print('Timestamp: ', stats['timestr'])
print('Elapsed time: ', stats['elapsed'])
print('Hosts up: ', stats['uphosts'])
print('Hosts down: ', stats['downhosts'])

# printing out scan
print('Services: ', info.get('tcp').get('services'))
print('Method: ', info.get('tcp').get('method'))

print(stats)
print(info)
print(xml)
