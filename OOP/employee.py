#A class is a blue print for creating Objects
##Remember that using our classes we are modelling real types(where attributes and methods come in)
class Employee:
   
   #self signifies the instance
   def __init__(self,first,last,pay):
       self.first=first
       self.last=last
       self.pay=pay
       self.email=f'{first}{last}@company.com'

   #every method in a class takes in the instance as the first argument
   def full_name(self):
       return '{}{}'.format(self.first, self.last)



#an object is simply an instance of a class
#When i create different objects from the same class
# both are unique instances

emp_1=Employee('Caleb', 'Mbugua',90000)
emp_2=Employee('Mercy', 'Wanjiru',70000)



print(emp_1.email)
print(emp_2.email)

print(emp_1.full_name())
print(emp_2.full_name())

##I can also call my methods directly from my class
##when doing this i have to pass the full instance of the class
print(Employee.full_name(emp_1))
print(Employee.full_name(emp_2))


##I may add my instances manually but this is not the recommended approach
##the best way is to have an init method
##I can therefore have the attributes of my class set at instantiation
##instance variables
##Each class has got variables that are unique to the class
##these are variables that are unique to each instance

# emp_1.first='Caleb'
# emp_1.last='Mbugua'
# emp_1.email='mbuguacaleb30@gmail.com'
# emp_1.pay=50000

# emp_2.first='Mercy'
# emp_2.last='Wanjiru'
# emp_2.email='wanjirumercy@gmail.com'
# emp_2.pay=50000

