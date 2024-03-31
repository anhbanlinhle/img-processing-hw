import numpy

M, N = map(int, input().split())
array = numpy.array([list(map(int, input().split())) for _ in range(M)])

print(array.transpose())
print(array.flatten())