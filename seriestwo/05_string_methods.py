course ='Python for Beginners'

##May also be used in lists as well
##It is general purpose
print(len(course))


##String specific methods
print(course.upper())
print(course.lower())

##Fiding a character in a string
##IT WILL RETURNT THE INDEX OF THE OCCURRENCE OF THIS CHARACTER
##IN OUR STRING
##THE FIND METHOD IS CASE SENSITIVE
print(course.find('P'))
print(course.find('o'))

##We can pass a sequence of characters
#returns the index
print(course.find('Beginners'))


##N/B
#These string methods return a completely new string
##they do not alter the prevoius string unless you reassign
print(course.replace('Beginners','Absolute Beginners'))

print(course.replace('P','J'))

##check whether sequence of characters is in a string
#Returns true or false
print('python' in course)

 