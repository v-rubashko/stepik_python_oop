class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + " " + self.surname

    def set_fullname(self, full_name):
        self.name, self.surname = full_name.split()

    fullname = property(get_fullname, set_fullname)


person = Person('Алан', 'Тьюринг')

person.surname = 'Вирт'
print(person.fullname)