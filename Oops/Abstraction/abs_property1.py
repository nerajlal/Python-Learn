from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    rect = Rectangle(width=5, height=10)
    circle = Circle(radius=3)

    print(f"Rectangle area: {rect.area}")   
    print(f"Circle area: {circle.area:.2f}")   