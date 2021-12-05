"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа
и выведите результат работы этой функции.
"""
import math


def distance():
    result = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return result


x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
print(distance())