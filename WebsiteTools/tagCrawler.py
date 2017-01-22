#! usr/bin/env python3

# this requires that the user already has a html file locally and in the same directory as this script

# importing html for parsing
from html.parser import HTMLParser

# creating object parse for parsing html
parse = HTMLParser()

# getting file from user and atempting to open
file = input("HTML file: ")
try:
    data = open(file,mode='r')
except FileNotFoundError:
    print("File not found")
    print('exiting...')
    exit()
except:
    print("Error opening file")
    print('exiting...')
    exit()

# feeding data to parser
print(parse.feed(data = str(data.read)))
# closing file
data.close()

