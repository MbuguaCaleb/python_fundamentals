# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Very similar to object literal in javascript..

# create dict
person = {
    "first_name": 'Caleb',
    "last_name": "Mbugua",
    'age': 25
}

# create using a constructor
person2 = dict(fist_name="Caleb", last_name="Mbugua", best_thing="Born Again")


# Access a single Value
# How i will be extracting my data after querying from an API
print(person['first_name'])

# Method2
print(person.get('last_name'))


# Add Key Value
# Remember i am adding a key value pair
person['phone'] = '254-704-699-193'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copying a dictinary
person2 = person.copy()
person2['city'] = 'Naivasha'

# remove an item
del(person['age'])

# Method2 remove item
person.pop("phone")

# clear
person.clear()

# length
print(len(person2))

# list of dict
people = [
    {'name': 'Mercy', 'age': 24},
    {'name': 'Humphrey', 'age': 58}
]

# Get item in the List of Dictionaries
print(people[1]['name'])

#print(people)
# print(person)
#print(person, type(person))
#print(person2, type(person2))
