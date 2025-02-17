import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = self._radius**2 * math.pi

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))