from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _int_format(obj):
        print(f'Целое число: {obj}')

    @format.register(float)
    @staticmethod
    def _float_format(obj):
        print(f'Вещественное число: {obj}')

    @format.register(tuple)
    @staticmethod
    def _tuple_format(obj):
        print('Элементы кортежа:', end=" ")
        print(*obj, sep=', ')

    @format.register(list)
    @staticmethod
    def _list_format(obj):
        print('Элементы списка:', end=" ")
        print(*obj, sep=", ")

    @format.register(dict)
    @staticmethod
    def _dict_format(obj):
        print('Пары словаря:', end=" ")
        print(*[(key, value) for key, value in obj.items()], sep=", ")

Formatter.format(1337)
Formatter.format(20.77)
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)