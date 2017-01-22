#! usr/bin/env python3

# importing getpass for password input
import getpass

# hardcoded username and password
username = 'username'
password = 'password'

###################################
# functions for getting inputs    #
###################################
# function for getting username
def getUName():
	uIn = input("Username: ")
	return uIn
# function for getting password
def getPWord():
	pIn = getpass.getpass("Password: ")
	return pIn

##############################################################
# functions for checking the values of username and password #
##############################################################
# checking username
def unameCheck(uname):
	if username == uname:
		return True
	else:
		return False
# checking password
def pwordCheck(pword):
	if password == pword:
		return True
	else:
		return False

#####################################################
# function for the actual login						#
#####################################################
# this function is used so that this script can be used by other scripts and get results
def login(uIn, pIn):
	# uses userIn and passIn, which are assigned later on in the code
	if unameCheck(userIn) and pwordCheck(passIn):
		return True
	else:
		return False

######################################################
# getting login information from user 				 #
######################################################
# getting username
userIn = input('USERNAME: ')
# getting password
passIn = input('PASSWORD: ')

########################################################
# checking Username and password 					   #
########################################################
if login(userIn, passIn):
	print('LOGIN SUCCESSFUL')
else:
	print('LOGIN FAILED')
# using function so that this script can be run by other scripts
login(userIn, passIn)
