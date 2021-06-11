import math
def print_square(height,width):


   
    width="*" * width + "\n"

    shape=''

    for i in range(height):
        shape+=width
     
    return shape
    
print(print_square(4,8))



shape=[4,2]

def no_of_shapes(shape):
    
    height=10
    width=7

    sq_height,sq_length=shape

    area_sq=sq_height*sq_length

    area_rectangle=height*width
    

    return math.floor(area_rectangle/area_sq)
    

print(no_of_shapes(shape))









