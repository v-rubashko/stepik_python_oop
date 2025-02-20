from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _num_neg(obj):
        return -1 * obj

    @neg.register(bool)
    @staticmethod
    def _bool_neg(obj):
        return not obj

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

try:
    Negator.neg('number')
except TypeError as e:
    print(e)