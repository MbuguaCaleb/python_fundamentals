#Mechanism for reusing code
class Mammal:
    def Walk(self):
        print("walk")
 

#Dog class inerting from Mammal
#child class inherits all methods from the parent
#i may as well add my own custom methods specific to the class
class Dog(Mammal):
    def bark(self):
        print("bark")
 


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")



dog1=Dog()
dog1.Walk()

cat1=Cat()
cat1.be_annoying()




 
