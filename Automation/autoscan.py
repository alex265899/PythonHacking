#!usr/bin/env python3.5
# last edited 2/6/2017 by Alexander Chapman

# importing os to run commands
import os

# printing out targeted systems, which is currently only linux, and requirements
print('Supported systems: Linux')

# generates a string based off of an option and its value
def optionGen(base, value):
    return (base + ' ' + value)

# getting the address and port from the user
siteToScan = input('Address to scan: ')
ports = input('Ports: ')

# timing options
print('Timing options:\n'
      '0:T0\n'
      '1:T1\n'
      '2:T2\n'
      '3:T3\n'
      '4:T4\n'
      '5:T5\n')
while True:
    try:
        timing = int(input('Timing (0-5)?: '))
        break
    except BaseException:
        timing = 2
        break
print(timing)
# os detection
tempVar = input('OS Detection [Y/n]? ')
if tempVar == 'y' or tempVar == 'Y':
    osDetection = True
else:
    osDetection = False
tempVar = None

# interface
interface = input('What interface to use? ')

# ip proto scan -sO
tempVar = input('IP protocol scan [Y/n]? ')
if tempVar == 'y' or tempVar == 'Y':
    IPprotoScan = True
else:
    IPprotoScan = False
tempVar = None

# port version scan -sV
tempVar = input('Port version detection [Y/n]? ')
if tempVar == 'y' or tempVar == 'Y':
    portVersionDetection = True
else:
    portVersionDetection = False
tempVar = None


# top ports --top-ports NUMBER
tempVar = input("Scan top ports (press enter for none): ")
if tempVar != '':
    topPort = int(tempVar)
    tempVar = None
else:
    topPort = False
    tempVar = None

# scan consecutive -r
scanConsecutive = input('Scan ports consecutively [Y/n]: ')
if scanConsecutive == 'y' or scanConsecutive == 'Y':
    scanConsecutive = True
else:
    scanConsecutive = False

# fast scan -F
fastScan = input('Fast Scan [Y/n]: ')
if fastScan == 'y' or fastScan == 'Y':
    fastScan = True
else:
    fastScan = False

# ping scan -sn
pingScan = input('Ping scan [Y/n]: ')
if pingScan == 'y' or pingScan == 'Y':
    pingScan = True
else:
    pingScan = False

# ipv6 scanning -6
ipv6Scan = input("IPv6 Scan [Y/n]: ")
if ipv6Scan == 'Y' or ipv6Scan == 'y':
    ipv6Scan = True
else:
    ipv6Scan = False

# output -oA <basename>
outputFileBasename = input("Output file basename: ")

#================================
# generating the command
#================================
# base command
command = 'nmap '

# address
address = siteToScan
command = command + address

# timing option
timeTemplate = optionGen(' -T', str(timing))
command = command + timeTemplate

# os detection
if osDetection == True:
    command = command + ' -O'
else:
    pass

# interface
if interface != '':
    command = command + optionGen(' -e', interface)
else:
    pass

# ip proto scan
if IPprotoScan == True:
    command = command + ' -sO'
else:
    pass

# port version scan
if portVersionDetection == True:
    command = command + ' -sV'
else:
    pass

# top ports
if topPort != False:
    command = command + optionGen(' --top-ports', str(topPort))
else:
    pass

# scan consecutive
if scanConsecutive == True:
    command = command + ' -r'
else:
    pass

# fast scan
if fastScan == True:
    command = command + ' -F'
else:
    pass

# ping scan
if pingScan == True:
    command = command + ' -sn'
else:
    pass

# ipv6 scan
if ipv6Scan == True:
    command = command + ' -6'
else:
    pass

# output results to the three most common file types with a given basename
command = command + optionGen(' -oA', outputFileBasename)

###########################
# outputting final command
###########################
print(command)