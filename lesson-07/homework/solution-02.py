"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки
городов в этих странах. Написать функцию которая осуществляет поиск по городу и возвращает
страну. Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


def country(city):

    for countries, cities in countries_city.items():
        if city in cities:
            print(f"{city} city in {countries}")


if __name__ == "__main__":
    countries_city = {
        "Germany": ["Berlin", "Hamburg", "Munich", "Cologne"],
        "Belarus": ["Minsk", "Vitebsk", "Grodno", "Brest"],
        "Russia": ["Moscow", "Novosibirsk", "St.Petersburg"],
        "France": ["Paris", "Marseille", "Lyon"]
    }

    city = input("Enter the city of interest: ")
    country(city)
