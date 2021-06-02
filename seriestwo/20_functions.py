
# #function parameters 
# #parameters are what we define in inside our function
# def greet_user(first_name,last_name):
#     print(f'Hi {first_name} {last_name}')
#     print("Welcome Aboard")


# ##Arguments are what we Supply to Our functions
# print("Start")
# greet_user("caleb","Mbugua")
# greet_user("Mary","Wanjiru")
# print("Finish")


# ##Key word arguments

# ##for positional arguments the position and order matters for example in the above caleb will always
# ##be first name and mbugua will be last name

# ##We also have key word argments whose position doesnt matteer

# ##With KeyWord arguments we do not have to worry about the order of our parameters
# print("Start")
# #we go fully explicit when using Key word arguments
# greet_user(last_name="caleb",first_name="Mbugua")

# greet_user(last_name="Mary",first_name="Wanjiru")

# print("Finish")
 

##Keyword arguments improve the readability of my code grearly in some instances
##Example when my function only contains numbers andit is hard to distinguish 

##When mixing keyword arguments we should always start with positional arguments


##return statemet
def square(number):
    return number*number

print(square(3))