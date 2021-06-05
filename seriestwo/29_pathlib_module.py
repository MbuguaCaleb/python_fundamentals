from pathlib import Path

##Absolute--->With ABsolute Paths we begin from the Root of Our Hardisk

##C:\ProramFiles--->windows

##Mac or Linux
##usr/local/bin


##Relative--->With Relative Paths We begin from the Root of the
##files that we are currently in


##Remeber that Path for this case has been imported as a class

##Case One->NO ARGUMENT(It is going to reference the path directory)

# Path()

##If we pass ecommerce it is going to reference that directory
path=Path("seriestwo/packages/ecommerce")

#Methods we can call

print(path.exists())

##create a directory
##startting from wehre i am it is going to make a directory
# path=Path("emails")
# print(path.mkdir())

##Removing a directory
# path=Path("emails")
# print(path.rmdir())


##Searching within my directories
path=Path('seriestwo')

# for file in path.glob('*.py'):
#     print(file)

##we can use differennt extensions as well such as *txt,.xls

##Prints everything in My current Path
for file in path.glob('*'):
    print(file)
 