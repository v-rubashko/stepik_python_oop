import math


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if self.b**2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.b**2 - 4 * self.a * self.c)) / (2 * self.a)

    @property
    def x2(self):
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / (2 * self.a)

    @property
    def view(self):
        temp = {True:"+", False:"-"}
        b_sign = self.b >= 0
        c_sign = self.c >= 0
        return f"{self.a}x^2 {temp[b_sign]} {abs(self.b)}x {temp[c_sign]} {abs(self.c)}"


    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients


polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)