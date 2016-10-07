# get_requests.py
# usr/bin/python27 Python 2.7

# importing request library
import requests

# setting the req variable
req = requests.get(raw_input("Complete URL: "))

# printing out the response code
print "Response Code: " + str(req.status_code) + '\n'
# printing out headers
print "Headers: "
print req.headers
print ''
# printing out html
print "Response:\n" + req.text
