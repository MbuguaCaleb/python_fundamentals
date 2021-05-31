#The inner loop must complete first the we go to other loop
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

 

numbers =[2,2,2,2,5]


for number in numbers:
    stringNum=''
    for num in range(number):
        stringNum +='x'
    print(stringNum)
    
 
      

