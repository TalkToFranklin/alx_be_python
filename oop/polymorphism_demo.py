import math

class Shape:
    def area(self):
        # Raises a NotImplementedError indicating derived classes need to override this method.
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        # Initialize a Rectangle instance with length and width. 
        self.length = length
        self.width = width

    def area(self):
        # Calculate the area of the rectangle. 
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        # Initialize a Circle instance with a radius.
        self.radius = radius

    def area(self):
        # Calculate the area of the circle. 
        return math.pi * (self.radius ** 2)