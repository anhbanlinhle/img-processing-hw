import numpy

def rev(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = rev(arr)
print(result)