import numpy as np

N, M, P = map(int, input().split())

array1 = np.array([list(map(int, input().split())) for i in range(N)])
array2 = np.array([list(map(int, input().split())) for i in range(M)])

result = np.concatenate((array1, array2), axis=0)

print(result)