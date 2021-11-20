"""
Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""


def my_function():
    for name in my_names:
        print(f"Hello, {name}")


my_names = ["Alex", "Victor", "Roma", "Maria", "Slava"]
print(my_function())
