#!usr/bin/env python27
import base64

#============================================
# Base64
# Encoding string to base64
def base64_encode(x):
    try:
        return base64.b64encode(x)
    except BaseException:
        return "Encryption Not Possible"

# Decoding string from base64
def base64_decode(x):
    try:
        return base64.b64_decode(x)
    except BaseException:
        return "Decryption not possible"
# =============================================
# Base32
# Encoding string to base32
def base32_encode(x):
    try:
        return base64.b32encode(x)
    except BaseException:
        return "Encryption not possible"

# Decoding string from base32
def base32_decode(x):
    try:
        return base64.b32decode(x)
    except BaseException:
        return "Decoding not possible"
# ============================================
# Base16
# Encoding string to base16
def base16_encode(x):
    try:
        return base64.b16encode(x):
    except BaseException:
        return "Encryption not possible"

# Decoding from base16
def base16_decode(x):
    try:
        return base64.b16decode(x)
    except BaseException:
        return "Decryption not possible"

print "Base64/32/16 Encoding/Decoding"
usrInput = raw_input("String >>> ")


# setting newline variable
linebreak = "====================================================="
print linebreak

print "Base64 Results:"
print "     Encryption: {}".format(base64_encode(usrInput))
print "     Decryption: {}".format(base64_decode(usrInput))
print linebreak
print "Base32 Results:"
print "     Encryption: {}".format(base32_encode(usrInput))
print "     Decryption: {}".format(base32_decode(usrInput))
print linebreak
print "Base16 Results"
print "     "