"""
Написать функцию принимающая на вход неопределенным количеством аргументов и
именованный аргумент func_type.
В зависимости от func_type вернуть минимальное
либо максимальное значение. Написать программу в виде трех функций.
"""


def my_funcion_max(*args, func_type):  # Выводит максимальное значение из всех введенных
    print(max(my_list))


def my_funcion_min(*args, func_type):  # Выводит все введенные значения
    print(min(my_list))


def my_funcion_list(*args, func_type):  # Выводит минимальное значение из всех введенных
    print(" ".join(my_list))


my_list = input("Введите список чисел через Space. По завершению нажмите Enter: ").split()
func_type = input("Введите\n"
                  "list - если хотите вывести весь список;\n"
                  "max - если хотите вывести максимальное значение из списка;\n"
                  "min - если хотите вывести минимальное значение из списка: ")

if func_type == "max":
    my_funcion_max(my_list, func_type="max")
if func_type == "min":
    my_funcion_min(my_list, func_type="min")
if func_type == "list":
    my_funcion_list(my_list, func_type="list")
