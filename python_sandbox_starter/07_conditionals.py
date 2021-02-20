# If/ Else conditions are used to decide to do something based on something being true or false
x = 50
y = 30


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# We do not have to put in the brackets when comparing the conditions

# Simple if
# if x > y:
#     print(f'{x} is greater than {y}')


# if/else
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')


# elif
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     # one equals is for assignment
#     # two equals are used to compare values
#     print(f'{x} is equals to {y}')
# else:
#     print(f'{y} is greater than {x}')


# Nested if
# Its however not adivisable to Nest Mutiple If Statements
# Its better to use logical operators
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than 10')


# Logical operators (and, or, not) - Used to combine conditional statements

# and
# both conditions have to be true
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less than 10')

# # or
# if x > 2 or x <= 10:
#     print(f'{x} is greater than 2 or less than 10')

# # not
# if not(x == y):
#     print(f'{x} is not equal to {y}')

# N/B
# Comparison operators always evaluate to true or false and only run when true

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object(List)
numbers = [1, 2, 3, 4, 5]

# in
# if x in numbers:
#     print(x in numbers)

# # not in
# if x not in numbers:
#     print(x not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
# if x is y:
#     print(x is y)


# is not
if x is not y:
    print(x is not y)
