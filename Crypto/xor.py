import sys

def file(name):
	newFile = open(name, mode='r')
	contents = newFile.read()
	newFile.close()
	return contents

plaintext = input("Plaintext File: ")
password = input("File to encrypt with: ")
write_to = input("Write to file (must already be created): ")

plaintext = file(plaintext)
password = file(password)


result = ""

while len(plaintext) != len(password):
	for item1, item2 in zip(plaintext, password):
		if len(plaintext) > len(password):
			password = password + item2
		if len(plaintext) < len(password):
			plaintext = plaintext + item1
		if len(password) == len(plaintext):
			break

for item1,item2 in zip(plaintext,password):
	item1 = ord(item1)
	item2 = ord(item2)
	xored = item1^item2
	sys.stdout.write("\r %s" % chr(xored))
	result = result + chr(xored)



resultFile = open(write_to, 'w')
resultFile.write(result)
resultFile.close()

