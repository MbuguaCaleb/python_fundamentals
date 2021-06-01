names=['John','Caleb','Mbugua','Karanja']

print(names)

print(names[0])
print(names[2])

##Print from the end of the List
print(names[-1])
print(names[-2])

##Range of Items
print(names[2:])

##last item in the index is not returned
print(names[2:4])

print(names[:])

##Each mofifications returns a new list
names[1] ='kimani'

print(names)


numbers =[1,2,3,4,5,7,3,90,2]

currentNumber=numbers[0]
for number in numbers:
    if number >currentNumber:
        currentNumber=number

print(currentNumber)


