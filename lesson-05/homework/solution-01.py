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
    for i in range(len(args)):
        if args[i] != None:
            arguments.append(f"var{i+1} = {args[i]}")
    arguments2 = ", ".join(arguments)    #склеим список для вывода
    print(f"Переданы аргументы: {arguments2}")


var1 = input()
var2 = input()
var3 = input()
three_args(var1, var2, var3)
