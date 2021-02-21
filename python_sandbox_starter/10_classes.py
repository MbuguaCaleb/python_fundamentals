# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
    # Constructor
    # Runs when you instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Any method inside a class Must take in Self
    def greeting(self):
        return f'My  name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend Class
# You pass the class you are extending from as a Parameter
class Customer(User):
    # Runs when you instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # Method Overriding
    # When you have exactly the same method name in child class as in the parent
    def greeting(self):
        return f'My  name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init user object
# Instantiating an object from a class
caleb = User('Mbugua Caleb', 'mbuguacaleb30@gmail.com', 25)

# Init Customer Object
mercy = Customer("Wanjiru Kerei", 'wanjirukerei@gmail.com', 30)

mercy.set_balance(500)

# Calling a Method from a Parent Class
print(mercy.greeting())

# print(caleb.name)
# print(caleb.age)
# print(caleb.email)

# calling a Method
caleb.has_birthday()
# print(caleb.greeting())
