# post_requests.py
# usr/bin/python27 Python 2.7

# importing requests module and json module
import requests
import json

while True:
    try:
        # getting complete URL from user
        url = input("Complete URL: ")

        # saving requests.post(url) to var req
        req = requests.post(url=url)
        break
    except requests.exceptions.MissingSchema:
        print("Invalid URL. Be sure to put HTTP or HTTPS in the url too. Try again!")

# getting the response headers and parsing them from dictionary
response_headers = req.headers

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# returning some data about the url
print("<<<QUICK INFO>>>")
print("Encoding: {0}\n".format(req.encoding))
print("Response Code: {0}\n".format(req.status_code))
# parsing response header dictionary
print("Header           Value")
print("-"*50)
for key in response_headers:
    print(key)
    print("                 " + response_headers[key])
    print("_"*50)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# data settings
print("<<<DATA/PAYLOAD SETTINGS>>>")

# determining whether to read data from file or from console
read_from_file = input("Read data from file [Y/n]: ")
read_from_file = read_from_file.lower()
if read_from_file == 'y':
    print("Data in file should be in python dictionary format ({'key' : 'value'})")
    # getting file name and then reading file to var request_data
    while True:
        try:
            file_name = input("File name (in same directory): ")
            file = open(file_name, mode='r')
            break
        except IOError:
            print("Incorrect file name. Be sure it is in the same directory as this program. Try again")
    request_data = file.read()
elif read_from_file == 'n':
    print("Data should be in dictionary format ({'key' : 'value'})")
    request_data = input("Data: ")
else:
    request_data = "null"
    print("No data given. Continuing")

if request_data == "null":
    pass
else:
    # determining if data should be in json format
    is_json = input("Should data be JSON formatted [Y/n]: ")
    is_json = is_json.lower()

    if is_json == 'y':
        request_data = json.dumps(request_data)
    elif is_json == 'n':
        pass

