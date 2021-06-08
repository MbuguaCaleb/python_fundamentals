##Allows us to inherit attributes and methods from our parent classes.

##We are able to create subclasses with all the functionality of the parent class
##then override and add new functionality without affeecting the parent class in anyway
class Employee:
   
   raise_amount=1.04

   def __init__(self,first,last,pay):
       self.first=first
       self.last=last
       self.pay=pay
       self.email=f'{first}{last}@company.com'

   def full_name(self):
       return '{}{}'.format(self.first, self.last)

   def apply_raise(self):
       self.pay=int(self.pay * self.raise_amount)
       

#We are able to make changes in our sub classes without worrying about breaking anything from our parent class
class Developer(Employee):
    raise_amount=10

    #when adding more attributes to our child class, we should add a constructor 
    def __init__(self, first, last, pay,prog_lang):
        #line below calls the parent init method such that i do not have to 
        # repeat myself
        #The below lines call the parent init method
        super().__init__(first, last, pay)
        # Employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang


class Manager(Employee):
    #init method can also have default params that are called if i do not pass the values    
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees =[]
        else:
            self.employees=employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("---->",emp.full_name())


#Developer inerited all the methods in employee as well
dev_1=Developer('Caleb', 'Mbugua',9000,'Python')
dev_2=Developer('Mercy', 'Wanjiru',70000,'Java')

mgr_1=Manager('Sue','Smith',90000,[dev_1])

# print(dev_1.email)
# print(dev_1.prog_lang)


# mgr_1.add_employee(dev_2)

# print(mgr_1.email)

# mgr_1.remove_employee(dev_1)

# mgr_1.print_emps()


#conclusion
# is_instance and is_subclass methods

print(isinstance(mgr_1,Employee))

print(isinstance(mgr_1,Developer))


##issublcass
print(issubclass(Developer,Employee))
print(issubclass(Developer,Manager))


# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
##This method helps me see Method resolution order(How inheritance occurs in the class including the hieracy and the inherited methods)
# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)
