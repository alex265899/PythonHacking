#! /usr/bin/env python3.4

"""
TODO:
    Nothing at the moment
"""

# import base64 module


# Encryption class
class Encryption:
    # base64
    def bs64(string):
        return base64.b64encode(string)

    # base32
    def bs32(string):
        return base64.b32encode(string)

    # base16
    def bs16(string):
        return base64.b16encode(string)


# decryption class
class Decryption:
    # base64
    def bs64(string):
        return base64.b64decode(string)

    # base32
    def bs32(string):
        return base64.b32decode(string)

    # base16
    def bs16(string):
        return base64.b16decode(string)

# getting input from the user
usrInput = input("String: ")

# printing out all results of possible decryption and encryption

#Decryption results
print("Decryption")
print("Base64: ", Decryption.bs64(usrInput))
print("Base32: ", Decryption.bs32(usrInput))
print("Base16: ", Decryption.bs16(usrInput))

#Seperator
print("#"*50)

#Encryption results
