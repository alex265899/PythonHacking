#!usr/bin/env python3.5
# importing psutil for getting network statistics
import psutil as net
# importing matplotlib for live plotting
import matplotlib.pyplot as plt

def getinterfaces():
    stat_results = net.net_if_stats()
    return stat_results.keys()

def getspeed(name):
    net_info = net.net_if_stats()
    try:
        net_speed = net_info[name].speed
        return net_speed
    except KeyError:
        return 'Network interface does not exist'

# printing out available interfaces
print('Interfaces')
for value in getinterfaces():
    print(value)
# getting the name of the network interface to plot
if_name = input("Network interface name: ")
print(getspeed(if_name))
