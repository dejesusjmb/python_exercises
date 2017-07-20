import math
from abc import ABCMeta, abstractmethod


class Shape(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        return math.pi * (self._radius ** 2)


class Rectangle(Shape):
    def __init__(self, height, length):
        self._height = height
        self._length = length

    def get_area(self):
        return self._height * self._length

class Triangle(Shape):
    def __init__(self, base, height):
        self._height = height
        self._base = base

    def get_area(self):
        return self._height * self._base * 0.5


def sum_area_of_shapes(shapes):
    return sum([shape.get_area() for shape in shapes])
