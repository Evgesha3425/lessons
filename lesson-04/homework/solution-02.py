"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран. Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево
"""

my_string = input("Введите строку: ").lower()
if my_string == my_string[::-1]:
    print("yes")
else:
    print("no")
