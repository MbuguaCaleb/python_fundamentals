# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes

'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# no semicolons in python
# no declaration of int or $ before hand

# int automatically casted by default
x = 1

# float
y = 2.5

# Str can have single or double quotes.
name = 'JOHN'

# bool #always begin with T Capital or F false
is_cool = True


# Multiple Assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic Math
a = x+y

# Output something
print('Hello')

# Output Mutile thinfs
print(x, y, name, is_cool, a)

# Checking the Type of a variable
print(type(x))

# Casting
# convert from one datatype to another
x = str(x)
y = int(y)
z = float(x)

print(type(z), z)
