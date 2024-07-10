"""task1.py"""

import math

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def set_side_length(self, side_length):
        self.side_length = side_length

    def get_side_length(self):
        return self.side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

    def display_info(self):
        print(f"Square side length: {self.get_side_length()}")
        print(f"Square area: {self.area()}")
        print(f"Square perimeter: {self.perimeter()}")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        print(f"Circle radius: {self.get_radius()}")
        print(f"Circle area: {self.area()}")
        print(f"Circle circumference: {self.circumference()}")


class InscribedCircle(Square, Circle):
    def __init__(self, side_length):
        Square.__init__(self, side_length)
        Circle.__init__(self, side_length / 2)

    def display_info(self):
        Square.display_info(self)
        print(f"Inscribed Circle radius: {self.get_radius()}")
        print(f"Inscribed Circle area: {self.area()}")
        print(f"Inscribed Circle circumference: {self.circumference()}")


if __name__ == "__main__":
    inscribed_circle = InscribedCircle(10)
    inscribed_circle.display_info()
