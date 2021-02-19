# A List is a collection which is ordered and changeable. Allows duplicate members.

# There are other datatypes that are unordered and do not accept dupicate Members

# The Unique thing with python is that there is no prior declaration as happens in php and js and java

# We Must also terminate with a semi colon in python

# create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Method2
# Constructor
#numbers2 = list((1, 2, 3, 4, 5))


# Get a Value
print(fruits[0])


# Change a Value
fruits[0] = 'blueberries'

# Get Length
print(len(fruits))

# Append to the List
fruits.append('Mangoes')

# Remove from the List
fruits.remove('Grapes')

# Insert into position and not just append
fruits.insert(2, 'Strawberries')

# Remove from Position
fruits.pop(2)


# Reverse the List
fruits.reverse()


# Sorting Alphabetically
fruits.sort()

# Reverse the sort
fruits.sort(reverse=True)

print(fruits)
