class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Некорректное имя")

    def get_name(self):
        return self._name

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age in range(0, 111):
            self._age = new_age
        else:
            raise ValueError("Некорректный возраст")

    def get_age(self):
        return self._age


user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())