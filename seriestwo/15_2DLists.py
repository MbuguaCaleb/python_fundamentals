

##3 by 3 matrix 
##each item in a list is another list

##remember every item in list starts with index 0
matrix=[
    [1,2,3], 
    [4,5,6],
    [7,8,9]
] 

##This is How we access items in a 2D matric
print(matrix[0][1])

#change item on matrix
matrix[0][1] = 30

print(matrix)
print(matrix[2][2])

for row in matrix:
    ##will return each list in a Matrix
    for item in row:
        print(item)


