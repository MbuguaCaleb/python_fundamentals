# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager
# (including Django) as well as custom modules

# Importing a core python module which i do not have to install

# Core modules
import datetime
# importing only the date and not te whole class
from datetime import date
import time
from time import time


# PIP Modules
from camelcase import CamelCase

# Custom Module
# This is like making a custom utils class then importing it
# i am importing a method directly instead of importing a class
# importing the whole class will have extra steps(instantiation then calling)
from validator import validate_email


# today = datetime.date.today()
today = date.today()

timestamp = time()

# print(timestamp)


c = CamelCase()
print(c.hump('hello there world'))


email = 'test@test.com'
if validate_email(email):
    print('Email is Valid')
else:
    print('Email is Bad')


# Python has a package manager called PIP
# Just like npm in nodejs

# Use PIP 3 for python version three
# pip3 install camelcase

# You may install a package globally or in a virtual enviroment(via venv or pipenv)
# The package when installed in a virtual enviroment is just stored locally within
# the project

# So as to view installed packages is use the command pip freeze
# if i run pip freeze in a virtual environment it just shows me whats in that partucular
# enviroment
