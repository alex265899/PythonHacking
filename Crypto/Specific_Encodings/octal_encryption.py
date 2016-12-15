#/usr/bin/env python34

print("Please only enter a number only! Anything else will result in an error!")

# defining a function to return the octal of a number
def to_octal(x):
    try:
        x = int(x)
        return oct(x)
    except ValueError:
        return "Didn't give a number. Try again!"
    except BaseException:
        return "An error occurred!"

usr_input = input("Number >>> ")
print(to_octal(usr_input))

while usr_input != "":
    usr_input = input("Number >>> ")
    print(to_octal(usr_input))

print("Exiting...")