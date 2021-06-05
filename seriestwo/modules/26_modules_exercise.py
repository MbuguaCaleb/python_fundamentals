from utils import find_max


numberArray=[2,5,0,9]
numberArrayTwo=[900,300,32,123]
maxNum=find_max(numberArray)
maxNum2=find_max(numberArrayTwo)

print(maxNum)
print(maxNum2)


##Max is also build in function
##Its not goo practice to name our variables in the same way
print(max(numberArrayTwo))
print(max(numberArray))