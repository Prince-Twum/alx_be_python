import math

class Shape:
    def area(self):
        """Base method that must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override area()")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides Shape.area() for a rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides Shape.area() for a circle."""
        return math.pi * (self.radius ** 2)