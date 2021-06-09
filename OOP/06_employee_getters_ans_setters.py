##We define our first and last name as a method but we are able to access it as an attribute
# The property decorator allows us to define Class methods that we can access like attributes. This allows us to implement getters, setters, and deleters.
class Employee:
   
   def __init__(self,first,last,pay):
       self.first=first
       self.last=last
       self.pay=pay
     
   #using property decorator this email will be accessed as an attribute
   @property
   def email(self):
       return '{}.{}@email.com'.format(self.first,self.last)

   @property
   def fullname(self):
       return '{}{}'.format(self.first, self.last)

   #when i set the fullname i want to do the reverse which is set the first and the last
   @fullname.setter
   def fullname(self,name):
       first,last=name.split(' ')
       self.first=first
       self.last=last

   @fullname.deleter
   def fullname(self):
       print("Delete Name")
       self.first=None
       self.last=None

emp_1=Employee('Caleb','Mbugua',30000)
emp_2=Employee('Mercy','Wanjiru',9000)

emp_1.first='kigen'

emp_1.fullname='Humphrey Kimani'
##Without the getter the email does not update despite changing the fisrt name

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname


##When i want to make an attribute to a method we can easily implement the getters and setters so that 
#people using my code do not have to change how they 
#were calling attributes