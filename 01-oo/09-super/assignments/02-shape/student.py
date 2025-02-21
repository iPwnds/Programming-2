from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
<<<<<<< HEAD
        pass
=======
        ...
>>>>>>> 4b673df (completing part 08 (overriding))

    @property
    @abstractmethod
    def perimeter(self):
<<<<<<< HEAD
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self.length

class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius):
        self._major_radius = major_radius
        self._minor_radius = minor_radius

    @property
    def major_radius(self):
        return self._major_radius

    @property
    def minor_radius(self):
        return self._minor_radius

    @property
    def area(self):
        return self.major_radius * self.minor_radius * pi

    @property
    def perimeter(self):
        raise NotImplementedError("Perimeter formula for an ellipse is complex and not implemented.")

class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)

    @property
    def radius(self):
        return self.major_radius

    @property
    def perimeter(self):
        return 2 * self.radius * pi
=======
        ...
>>>>>>> 4b673df (completing part 08 (overriding))
