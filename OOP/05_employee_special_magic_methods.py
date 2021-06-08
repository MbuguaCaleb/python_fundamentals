#They help change our objects are printed and displayed

class Employee:

   raise_amount = 1.04
   
   def __init__(self,first,last,pay):
       self.first=first
       self.last=last
       self.pay=pay
       self.email=f'{first}{last}@company.com'

 
   def full_name(self):
       return '{}{}'.format(self.first, self.last)

 
   def apply_raise(self):
       self.pay=int(self.pay*self.raise_amount)


    #An ambiguous representatio of an object for logging and debugging
    #more for developers
    #best  practice for this method is to return something that will recreate the same object
   def __repr__(self):
       return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
   
   #brings a more readable represtation of the object to the end user
   def __str__(self):
       return '{}-{}'.format(self.full_name(),self.email)

   def __add__(self,other):
       return self.pay + other.pay

   #dunder method that will return the length of the fullname
   def __len__(self):
       return len(self.full_name())

emp_1=Employee('Caleb', 'Mbugua',90000)
emp_2=Employee('Mercy', 'Wanjiru',70000)

#No wonder they are called magc methods
print(emp_1+emp_2)
##They allow us to emulate some built in behaviour from within python

##By defining our own methods we are able to change this built in behaviour
##and methoods

##These methods have double underscores(Which  is refereed to as Dunder)

print(emp_1)


#i can as well call these methods separately

# print(str(emp_1))
# print(repr(emp_1))


# print(emp_1.__str__())
# print(emp_1.__repr__())
##Overides the functionality of the class from returning

# <__main__.Employee object at 0x000001AEE2935B50>

#to what i have specified in my these methods

# CalebMbugua-CalebMbugua@company.com


##Other built in dunder methods

print(1+2)
print('a'+'b')

##There is a magic method that simulates this differenty for integers and strings while printing to have differenct outputs

print(int.__add__(1,2))
print(str.__add__('a','b'))


##dunder LEN
print(len('caleb'))

# Also uses a dunder method in the background
print('caleb'.__len__())

print(len(emp_1))