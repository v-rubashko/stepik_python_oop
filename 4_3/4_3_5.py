from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = self.radius **2 * pi

circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)