class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iter_obj):
        return cls(*iter_obj)

    @classmethod
    def from_str(cls, str_obj):
        iter_object = (float(x) for x in str_obj.split())
        return cls.from_iterable(iter_object)

polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)

