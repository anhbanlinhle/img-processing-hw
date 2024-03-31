import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        #code cua ban o day
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        #code cua ban o day
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)
        
    def __mul__(self, no):
        #code cua ban o day
        real = self.real*no.real - self.imaginary*no.imaginary
        imaginary = self.real*no.imaginary + self.imaginary*no.real
        return Complex(real, imaginary)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    a = map(float, input().split())
    b = map(float, input().split())
    x = Complex(*a)
    y = Complex(*b)
    print('\n'.join(map(str, [x+y, x-y, x*y])))