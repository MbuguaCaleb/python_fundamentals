# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Caleb'
age = 25


# concatenate
# python can only concatenate strings and not integers.
# Every value must be casted to a string when being concatenated

#print('Hello, my name is ' + name + 'and age is' + str(age))


# String Formatting

# Better ways to format

# Arguments by position
#print('My name is {name} and i am {age}'.format(name=name, age=age))

# F-Strings
print(f'Hello, my name is {name} and i am {age}')


# String Methods
s = 'helloworld'

# Captialize string
print(s.capitalize())

# Make all upperCase
print(s.upper())

# make all lower
print(s.lower())

# swap case
print(s.swapcase())

# Get length
print(len(s))
# can be used in any other datatypes as well eg lists

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
# retuns true of fale based on what it starts with
print(s.startswith('hello'))

# ends with
print(s.endswith('d'))

# split into a list
print(s.split())

# find position
print(s.find('r'))

# is all alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())
