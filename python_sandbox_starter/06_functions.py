# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')


# setting a default parameter
def bestThing(description='Know Jesus'):
    print(f'Getting to {description} ')


# return Values
def getSum(num1, num2):
    total = num1 + num2
    return total
    # variable is within function scope
    # Outside is the global scope
    # inside is the function scope


num = getSum(2, 4)
print(num)

#sayHello('Caleb Mbugua')
# running a function with default parameter set
# bestThing()

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


#function--->params----->result
getSum = lambda num1, num2:  num1+num2


print(getSum(20, 30))



