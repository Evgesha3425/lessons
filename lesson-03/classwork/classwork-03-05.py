"""
Найти в списке ниже количество не уникальных элементов.
"""

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]

print(len(my_list) - len(set(my_list)))