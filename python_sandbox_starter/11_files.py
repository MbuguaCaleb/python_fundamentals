# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name:', myFile.name)

# closed it means if we closed on within our script
print('Is Closed:', myFile.closed)
print('Opening Mode', myFile.mode)


# Write to file
myFile.write('I love python')
myFile.write('and JavaScript')
myFile.close()


# Append to File
# If the file had been created before
# If you dont append to a file that had been created before it overrides everything
myFile = open('myfile.txt', 'a')
myFile.write('I also like PHP')


# Read from File
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
