"""
Напишите лямбда-функуцию для перевода земных лет в марсианские.
Функция принимает число (возраст в земных годах), а возвращает  возраст в марсианских годах.
Результат выведите на экран.
При написании программы учитывайте, что год на Марсе длится 687 земных суток и что в каждом
земном году 365 земных суток
"""


years_earth = int(input("Введите количество земных лет: "))
years_mars = lambda years_earth: years_earth * 365 // 687
print(years_mars(years_earth))

