#Insteadof writing all our code in one place,we write down
#our code in multiple places
##Each file is called a module 

#Modules organise our code intomultiple files
#we make imports without the extension

import  converters

print(converters.lbs_to_kg(70))


##syntax two for importing modules
##We may import specific functions from the module

##cntrl + space(We see all the functions in the Module)

from converters import lbs_to_kg

##we can the call the function directly
##without prefixing converters

print(lbs_to_kg(230))

