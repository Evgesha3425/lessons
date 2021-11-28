"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает
название сезона, к которому относится этот месяц.
Например, передаем 2, на выходе получаем "Winter".
"""


def month_to_season(month):
    season = ""
    if month == '12' or month == '1' or month == '2':
        season = "winter"
    if month == '3' or month == '4' or month == '5':
        season = "spring"
    if month == '6' or month == '7' or month == '8':
        season = "summer"
    if month == '9' or month == '10' or month == '11':
        season = "autumn"
    return season


month = input("Введите номер месяца: ")
print(month_to_season(month))