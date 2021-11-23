"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных,
но только если они не равны None. Получим, например, следующее
сообщение: Переданы аргументы: var1 = 2, var3 = 10.
"""

#
# Что-то не так с if. Не могу сделать чтобы не добавлялся текст в случае None
#


def three_args(*args):
    arguments = []    #добавим сюда аргументы, если они соответсвтуют условию
    if var1.isdigit():
        arguments.append(f"var1 = {var1}")
    if var2.isdigit():
        arguments.append(f"var2 = {var2}")
    if var3.isdigit():
        arguments.append(f"var3 = {var3}")
    arguments_print = ", ".join(arguments)    #склеил для вывода
    print(f"Переданы аргументы: {arguments_print}")


var1 = input()
var2 = input()
var3 = input()
three_args(var1, var2, var3)
