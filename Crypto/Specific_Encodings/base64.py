#!usr/bin/env python27
import base64

def base64_encode(x):
    try:
        return base64.b64encode(x)
    except BaseException:
        return "Encryption Not Possible"

def base64_decode(x):
    try:
        return base64.b64_decode(x)
    except BaseException:
        return "Decryption not possible"

print "Base64 Functions..."
usrInput = raw_input("String >>> ")

while usrInput != "":
    print "Encoded: {}".format(base64_encode(usrInput))
    print "Decoded: {}".format(base64_decode(usrInput))
    usrInput = raw_input("String >>> ")
    