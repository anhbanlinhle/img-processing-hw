from functools import reduce
from fractions import Fraction

N = int(input())
fractions = [Fraction(*map(int, input().split())) for i in range(N)]

product = reduce(lambda x, y: x * y, fractions)

print(f'{product.numerator} {product.denominator}')