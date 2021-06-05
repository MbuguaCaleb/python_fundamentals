##We use classes to define new types

##Simple types
##Numbers,strings,booleans
##complex types Lists and dictionaries

#we use classes to model real objects

#Use Pascal naming convention
#Must always begin with capital

##Classes define new types,With the new types we can define new Objects

class Point:
    def move(self):
         print("move")

    def draw(self):
        print("draw") 


point1=Point()

##We may as well add attributes to a class
point1.x=1
point1.y=3

point1.draw()

print(point1.x)

#Each object is idepend
point2=Point()
print(point2.x)


##Objects are made of classes

##A class simply is like a blue print
##We make objects off classes 