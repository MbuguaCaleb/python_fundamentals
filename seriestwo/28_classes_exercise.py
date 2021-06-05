import random

class Dice:                 
    def roll(self):
        number1=random.randint(0,100)
        number2=random.randint(100,200)
        randomtuple=(number1,number2)

        ##When returning a tuple its not a must that you specify the brackets
        return (number1,number2)
        #return randomtuple




dice1=Dice()

print(dice1.roll()) 


##Pep8
##Pythob enhancement proposal
##Besst practices to format your code

