#A connstructor is a method that gets called  at the point of creating an OBJECT
#To fully define a class we Must give it attributes
#Attributes are defined the constructor
# class Point:
#      def __init__(self,x,y):
#          self.x=x
#          self.y=y

#      def move(self):
#         print("move")


#      def draw(self):
#          print("drink")
    


# point=Point(10,20)

# ##We can change the values of attributes after instantiating the class
# point.x=11

# print(point.x)



##Exercise
class Person:
    def __init__(self,name):
        self.name = name
    
    #with self as a parameter in my method
    #i have access to the class attributes
    def talk(self):
        print(f'I am {self.name}')


caleb=Person("Caleb")

print(caleb.name)
caleb.talk()