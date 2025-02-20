from functools import singledispatchmethod
from datetime import date, timedelta

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except ValueError:
            print("Аргумент переданного типа не поддерживается")

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_iter(self, birth_date):
        if len(birth_date) == 3:
            try:
                self.birth_date = date(birth_date[0], birth_date[1], birth_date[2])
            except:
                print("Аргумент переданного типа не поддерживается")
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        today = date.today()
        result = 0
        while today - timedelta(days=365)> self.birth_date:
            result += 1
            today = date(today.year - 1, today.month, today.day)
        return result

birth_dates = [
    [2020],
    (2020,),
    [2020, 1],
    [2020, 1, '1'],
    (2020, 1),
    (2020, 1, '1'),
    [2020, 1, 1, 1],
    (2020, 1, 1, 1),
    [2020, '1', '1'],
    [2020, '1', 1],
]

for birth_date in birth_dates:
    try:
        birthinfo = BirthInfo(birth_date)
    except TypeError as e:
        print(e)
