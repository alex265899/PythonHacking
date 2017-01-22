# usr/bin/python27 Python3.5

# importing request library
import requests

# setting the req variable
req = requests.get(input("Complete URL: "))

# printing out the response code
print("Response Code: " + str(req.status_code) + '\n')
# printing out headers
print("Headers: ")
print(req.headers)
print('')
# printing out html
print("Response:\n" + req.text)
