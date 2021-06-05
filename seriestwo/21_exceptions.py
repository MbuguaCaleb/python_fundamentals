##Used to handle errors(Exceptions)
##Exceptions are a way of catching my errors so as to make my  programme not crash/termiate with error
# try:
#     age=int(input('Age:'))
#     print(age)
# except ValueError:
#     print('Invalid value')


##We may as well have mutiple exceptions being caught from our programme where i expect more than one
try:
    age=int(input('Age:'))
    income=20000
    risk=income/age
    print(age)
except  ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')


