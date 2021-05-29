# temperature= 35

# if temperature == 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")



##
# One Equals = assigment
# Equality == (Two equals)
# Not Equal(!=)


# name=input('Please enter your name ' )

# if len(name) < 3:
#     print("Error!Name Must be at least three charaters long")
# elif len(name) >50:
#     print("Error!Name Must be at a maximum of 50 long")
# else:
#     print("Congratulations!Name Looks good")

##Dividinf by a double stroke returns the next whole number
weight = int(input('Weight '))

unit = input('L(bs) or K(g) :')

unit = unit.lower()

if unit == 'l':
    converted_weight= weight*0.45 
    print(f"You are {converted_weight} kilos")
else:
    converted_weight= weight / 0.45 
    print(f"You are {converted_weight} pounds")

  