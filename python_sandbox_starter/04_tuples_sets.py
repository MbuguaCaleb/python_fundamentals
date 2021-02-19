# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create Tuple
fruits = ('Apples', 'Oranges', 'grapes')

# Method2
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# When i have only one value in a tuple i must have a trailing comma
# Without including the comma it will be interpereted as a string
fruits2 = ('Apples',)


# Get Value
print(fruits[0])
# Just like in a list

# Can't change a value
#fruits[0] ='Pears'


# Delete a tuple
del fruits2

# Get Length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Because it is unordered and unindexed it cannot allow duplicate members

# It all depends on what i want to do and what i want to store

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
# The Key word here is in
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Add duplicate
# It does not throw an error but will not add a duplicate Member
fruits_set.add('Apples')

# Remove from set
fruits_set.remove('Grape')

# clear set
# removing the conents
# fruits_set.clear()

# Delete
# removing it completely
#del fruits_set

print(fruits_set)
