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

   
   def apply_raise(self):
       self.pay=int(self.pay*self.raise_amount)


   #We work with the class instead of instance when using this method
   @classmethod
   def set_raise_amt(cls,amount):
       cls.raise_amount=amount
       
   @classmethod
   def from_string(cls,emp_str):
       first,last,pay=emp_str.split('-')
       return cls(first,last,pay)

   #Do not take an instance or method as first argument 
   #Used when the method does not have to use an instance or the class
   #any where within the function
   @staticmethod
   def is_workday(day):
       if (day.weekday() == 5) or (day.weekday() == 6):
           return False
       return True

      



emp_1=Employee('Caleb', 'Mbugua',90000)
emp_2=Employee('Mercy', 'Wanjiru',70000)


#calling the classmethod
# Employee.set_raise_amt(1.09)


# #class methods as alternative constructors
# ##When i want to do some manipulation to the data
# ##then pass my instance,this is a very good candidate for a class method

# emp_str_1='Mbugua-Kimani-10000'
# emp_str_2='Kigen-Andrew-7000'
# emp_str_3='Lucy-Wamboi-30000'

# #class method as an aternative constructor
# new_emp_1=Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)


##Static Methods
#Are normal methods used in a class and they neither take the instance or the class
#as the first argument

import datetime
my_date=datetime.date(2021,6,5)

#There are times i want to call methods without necessarily having
#to instantate a class..I can call these from the class directly.
print(Employee.is_workday(my_date))


##They are methods that have a logical connection with the class



#i can also run my class method from and instance but this is not advisable

# emp_1.set_raise_amt(1.25)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#Regular methods in a class automatically take the instance as the first argument(self)

#class Methods take in the class as the first argument

#whenw e are working with class variables we are working with the class instead of the instance

#we add a decorator class