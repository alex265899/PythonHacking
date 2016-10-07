# /usr/bin/env python27

# defining the function to turn a number to hexadecimal. This also includes error handling.
def to_hex(x):
    try:
        x = hex(int(x))
        return x
    except ValueError:
        return "Integer not given!"
    except BaseException:
        return "An error occurred. Try again!"



print "This is for encrypting a number to hexadecimal. Please only enter a number!"


# getting the first number from the user to turn to hex. This is also used to start the loop.
usr_input = raw_input("Number >>> ")

# turning number to hex and printing it out. Starting loop after this.
print to_hex(usr_input)

while usr_input != "":
    usr_input = raw_input("Number >>> ")
    print to_hex(usr_input)
