##Converting from One datatype to Another
birth_year = input('Birth Year:')

##Whatever we type from the terminal is always treated as a string
##Even if we type a Number

age= 2021 - int(birth_year)


##Getting the type of variables
print(type(birth_year))

print(type(age))

print(age)

##Exercise

weight= input('What is Your Weight in Pounds? ')

weight_in_kgs = int(weight) * 0.453592

print('Your weight in Kilogrammes is' + str(weight_in_kgs))

print(f'Your Kilogrammes are {weight_in_kgs}')

