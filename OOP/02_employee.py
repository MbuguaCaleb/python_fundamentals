##class variables are variables shared among all instances of a class   
## Instance variables on the other hand are unique for each instance
##class variables  shoud be the same for each instance

class Employee:

   #class variable
   num_of_emps=0
   raise_amount = 1.04
   
   def __init__(self,first,last,pay):
       self.first=first
       self.last=last
       self.pay=pay
       self.email=f'{first}{last}@company.com'

       Employee.num_of_emps+=1

 
   def full_name(self):
       return '{}{}'.format(self.first, self.last)

   #even a class variable should be accessed from our instance(self)
   def apply_raise(self):
       self.pay=int(self.pay*self.raise_amount)


print(Employee.num_of_emps)

emp_1=Employee('Caleb', 'Mbugua',90000)
emp_2=Employee('Mercy', 'Wanjiru',70000)


print(Employee.num_of_emps)
#i can raise the amount for each employee individually
emp_1.raise_amount=1.05
#printing the name space so as to see everything in the class

#changing globally
Employee.raise_amount=1.7

#Important to note .
#My code first looks locally from my instance and if it does not find the attribute it uses 
#the one from my class

#this gives me greater power and control.

#to see the contents of  my class
# print(emp_1.__dict__)
# print(Employee.__dict__)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

