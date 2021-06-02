##used to store info in Key Value pars

##When i get a dict and stringify i get a JSON OBJECT,
##WHICH IS exactly like a ductionary but in string format 

#IN a dictionary we can store a bunch of key val ue pairs

#Each Key in a dict should be unique

# customer={
#     "name":"Mbugua Caleb",
#     "age":30,
#     "is_verified":True,
# }

# #1. accessing items in dict
# #Exactly as i would access items in an array but keys should be in quotations since they are strings

# print(customer["name"])

# #2. Passing a non existent Key
# #This resuls to a key error
# #print(customer["birthDate"])

# ##same error is returned when i mispell a Key
# #print(customer["Age"])

# ##None is an object in Python which represents the absence of a value

# ##When i use get and look for a non existent Key i find None.

# print(customer.get("birthdate"))

# ##The above two are ways that i can get a value from a given Key

# #3.Supplying a default value when i cannot get a Key
# ##When it misses birthdate it returns Jan 1 1995

# print (customer.get("birthdate",'Jan 1 1995')) 

# ##updating a Key
# customer['name']='Joseph Atela'

# print(customer['name'])


# ##Add a new Key
# customer['birth_date'] ='1995-28-08'


# print(customer)


