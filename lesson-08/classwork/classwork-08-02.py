"""
Оформить предыдущую задачу в виде программы, вынести функцию в отдельный файл, добавить комментарии с описанием.
"""

from library import CAR_LIST, filter_cars

if __name__ == "__main__":
    year = int(input("Year: "))
    print(filter_cars(CAR_LIST, year))
