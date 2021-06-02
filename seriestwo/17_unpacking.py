coordinates=(1,2,3)

x =coordinates[0]

y=coordinates[1]
z= coordinates[2]

print(x*y*z)


##Unpacking is like descturcting syntax
x,y,z=coordinates

print(x*y*z)

##Unpacking also works for lists
coordinatesTwo=[1,2,2,4]

x,y,z,p=coordinatesTwo

print(x*y*z*p)