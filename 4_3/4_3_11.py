class Numbers:
    def __init__(self):
        self.all_numbers = []

    def add_number(self, n):
        self.all_numbers.append(n)

    def get_even(self):
        return [i for i in self.all_numbers if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.all_numbers if i % 2 != 0]

numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())
