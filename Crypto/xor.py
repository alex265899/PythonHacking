def file(name):
	newFile = open(name, mode='r')
	contents = newFile.read()
	newFile.close()
	return contents

plaintext = input("Plaintext File: ")
password = input("File to encrypt with: ")
writeto = input("Write to file (must already be created): ")

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
	print(chr(xored))
	result = result + chr(xored)

print(result)
resultFile = open(writeto, 'w')
resultFile.write(result)
resultFile.close()

