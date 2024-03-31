import cmath

complex_number = complex(input())

r = abs(complex_number)
phi = cmath.phase(complex_number)

print(r)
print(phi)