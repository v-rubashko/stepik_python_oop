import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return math.sqrt(self.x**2 + self.y**2)

vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())