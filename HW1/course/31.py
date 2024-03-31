import numpy

numbers = list(map(int, input().split()))
array = numpy.array(numbers).reshape(3, 3)

print(array)