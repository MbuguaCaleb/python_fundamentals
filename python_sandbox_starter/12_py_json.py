# JSON is commonly used with data APIS.
# Here how we can parse JSON into a Python dictionary
# JSON IS PARSED INTO A PYTHON DICTIONARY SO THAT WE CAN WORK WITH IT

import json

# Sample JSON
userJSON = '{"first_name":"Caleb","last_name":"Mbugua","age":25}'

# Parse to dict
# converts JSON TO A DICTIONARY
user = json.loads(userJSON)

print(user)
# Remeber this is how we extract data from a dictionary
print(user['first_name'])


# DICT TO  JSON FORMAT
# OPOSITE
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1}
carJSON = json.dumps(car)

print(carJSON)


# Dictionary
# {'first_name': 'Caleb', 'last_name': 'Mbugua', 'age': 25}

# JSON

# {"make": "Ford", "model": "Mustang", "year": 1}
