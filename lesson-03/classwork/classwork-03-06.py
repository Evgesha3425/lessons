"""
Создать переменную содержащую сторону квадрата, создать новый список, в котором будут периметр квадрата, площадь
квадрата и диагональ квадрата.
"""

import math

square_side = 100

square_list = [
    square_side * 4,
    square_side * square_side,
    math.sqrt(square_side * square_side * 2),
]
print(square_list)