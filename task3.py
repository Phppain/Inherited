"""task3.py"""

import json

class Shape:
    def show(self):
        raise NotImplementedError("Subclasses should implement this method")

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(**data)


class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Square: Top-left corner ({self.x}, {self.y}), Side length {self.side_length}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Rectangle: Top-left corner ({self.x}, {self.y}), Width {self.width}, Height {self.height}")


class Circle(Shape):
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def show(self):
        print(f"Circle: Center ({self.cx}, {self.cy}), Radius {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Ellipse: Bounding box top-left corner ({self.x}, {self.y}), Width {self.width}, Height {self.height}")


if __name__ == "__main__":
    shapes = [
        Square(1, 2, 5),
        Rectangle(3, 4, 6, 8),
        Circle(5, 5, 3),
        Ellipse(2, 2, 7, 5)
    ]

    for i, shape in enumerate(shapes):
        shape.save(f"shape_{i}.json")

    loaded_shapes = []
    for i in range(len(shapes)):
        if isinstance(shapes[i], Square):
            loaded_shapes.append(Square.load(f"shape_{i}.json"))
        elif isinstance(shapes[i], Rectangle):
            loaded_shapes.append(Rectangle.load(f"shape_{i}.json"))
        elif isinstance(shapes[i], Circle):
            loaded_shapes.append(Circle.load(f"shape_{i}.json"))
        elif isinstance(shapes[i], Ellipse):
            loaded_shapes.append(Ellipse.load(f"shape_{i}.json"))

    for shape in loaded_shapes:
        shape.show()
