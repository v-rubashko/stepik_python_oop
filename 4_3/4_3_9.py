class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, m):
        self.right += m

    def add_left(self, m):
        self.left += m

    def get_result(self):
        if self.right == self.left:
            return 'Весы в равновесии'
        elif self.right < self.left:
            return 'Левая чаша тяжелее'
        else:
            return 'Правая чаша тяжелее'

scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())