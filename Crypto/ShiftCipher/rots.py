#usr/env/py27 Python2.7
import string.translate                                            # Importing the translate module for string shifting

alphabet = {                                                    # Assigning each letter in alphabet to a number
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '10',
    'k': '11',
    'l': '12',
    'm': '13',
    'n': '14',
    'o': '15',
    'p': '16',
    'q': '17',
    'r': '18',
    's': '19',
    't': '20',
    'u': '21',
    'v': '22',
    'w': '23',
    'x': '24',
    'y': '25',
    'z': '26'
}
while True:                                                        # Creating loop to make sure user inputs number
    rot_number = raw_input("Rot Value >>> ")
    try:
        int(rot_number)
        break
    except:
        print "Input a number"

string = raw_input("String >>> ")                                   # Getting the string to get rot value

for character in string:


                                                                    # Keep this blank line