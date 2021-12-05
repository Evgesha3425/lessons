"""
Написать функцию, которая перемещает два первых элемента списка в конец списка"
"""


numbers = [1, 2, 3, 4, 5]
def rotate(numbers):
    numbers = [*numbers[2:], *numbers[0:2]]
    return numbers
print(rotate(numbers))