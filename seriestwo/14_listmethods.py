numbers=[5,2,1,7,4]

#1.Add item to a list
numbers.append(30)

print(numbers)

#2.Add a number at a given Position
numbers.insert(0,10)

#3.remove item from a list
numbers.remove(7)
print(numbers)

#4.Empty the Whole list
#numbers.clear()
print(numbers)

#5.remove the last item in a list
numbers.pop()
print(numbers)

#6.chec for existenxe of item i list
print(numbers.index(5))

#print(numbers.index(50))

##METHOD 2
##returns a true or false
##same can be done for a  string
print(50 in numbers)


##7.Count occurrence of a item in a list
print(numbers.count(5))

##8.Sort items in a list
numbers.sort()
##none is returned when i print the result of a function with no return value
print(numbers)

#sort in descending order
numbers.reverse()

print(numbers)

#9.Copy of a list
numbers2=numbers.copy()
numbers.append(300)

print(numbers)
print(numbers2)


##exercise
##programme to remove duplicates in a list
##Do not confuse methods in python with PHP
listduplicate =[1,2,2,3,3,4,4,5,5,6,7,6,1,1]

for listItem in listduplicate: 
    if(listduplicate.count(listItem) > 0):
        listduplicate.remove(listItem)
    
print(listduplicate)

##solution two
numbers=[1,2,3,3,4,4,5,6,6,5,3,1,3]
unique=[]

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)