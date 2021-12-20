"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
методы: нахождение периметра и площади окружности), Triangle (атрибуты: три точки,
методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые методы не описанные в задании.
"""

import math


class Point:
    # x - horizontal coordinate
    # y - vertical
    def __init__(self, x1=0, x2=0, x3=0, y1=0, y2=0, y3=0):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3


class Figure(Point):
    pass


class Square(Figure):
    def __init__(self, x1, x2, y1, y2):
        super().__init__(x1, x2, y1, y2)

    def area_square(self):
        a = abs(self.x1 - self.x2)
        b = abs(self.y1 - self.y2)
        return a * b

    def perimeter_square(self):
        a = abs(self.x1 - self.x2)
        b = abs(self.y1 - self.y2)
        return 2 * a * b


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area_circle(self):
        return math.pi * (self.radius ** 2)

    def perimeter_circle(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):
    def __init__(self, x1, x2, x3, y1, y2, y3):
        super().__init__(x1, x2, x3, y1, y2, y3)

    def area_triangle(self):
        a = math.sqrt(((self.x1 - self.x2) ** 2) + (self.y1 - self.y2) ** 2)
        b = math.sqrt(((self.x2 - self.x3) ** 2) + (self.y2 - self.y3) ** 2)
        c = math.sqrt(((self.x1 - self.x3) ** 2) + (self.y1 - self.y3) ** 2)
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def perimeter_triangle(self):
        a = math.sqrt(((self.x1 - self.x2) ** 2) + (self.y1 - self.y2) ** 2)
        b = math.sqrt(((self.x2 - self.x3) ** 2) + (self.y2 - self.y3) ** 2)
        c = math.sqrt(((self.x1 - self.x3) ** 2) + (self.y1 - self.y3) ** 2)
        p = (a + b + c)
        return p
