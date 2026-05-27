from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    @property
    def area(self):
        print("Rectangle")

a = Rectangle()
a.area