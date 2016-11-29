import encodings
import string

def to_rot(x):          # Creating a function to return rot value
    try:                            # Exception handeling
        original_value = x
        return_value = original_value.encode("rot_13")      # Value to return (the new encoded one)
        return return_value                                 # Returning encoded string
    except BaseException:               # Handling errors
        return "Operation not possible"

while True:     # Creating a loop for the user to specify a file or string
    file_or_string = raw_input("[S]tring or [F]ile: ")
    file_or_string = file_or_string.lower()     # Converting to lowercase
    if file_or_string == 's' or file_or_string == 'f':                     # Checking the input, exiting the loop if it is OK
        break
    else:                                        # Asking the user to retry input if it is invalid
        print "Specify [S]tring or [F]ile"

if file_or_string == 'f':
    while True:
        filename = raw_input("Name of file (Must be in the same directory): ")      # Asking for file name
        try:
            opened_file = open(filename, mode='r')                                  # Attempting to open file
            fileContents = opened_file.read()                                       # reading file
            break
        except BaseException:                                                       # Handling exceptions
            print "File does not exist"
    print "New Text: \n {0}".format(to_rot(fileContents))                           # printing out the encoded contents of file

elif file_or_string == 's':         # If the user wants to encode a string
    string_input = raw_input("String to encode: ")
    print to_rot(string_input)

else:                       # If the user does not choose anything
    print "None chosen"
