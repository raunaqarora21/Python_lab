import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    k=numpy.array(arr,float)
return k
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)          
