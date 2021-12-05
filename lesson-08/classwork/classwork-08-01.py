"""
Дан список словарей. Каждый словарь описывает машину (серийный номер, цвет и год выпуска).
Создать функцию, которая возвращает новый список со всеми машинами, год выпуска которых больше Х.
"""


def filter_cars(car_list: list, year: int) -> list:
    result = []
    for car in car_list:
        if car["year"] < year:
            result.append(car)
    return result


if __name__ == "__main__":


    year = int(input("Year: "))
    print(filter_cars(car_list, year))



"""
if __name__ == "__main__":
    car_list = [
        {
            "serial": 123456,
            "color": "red",
            "year": 1999,
        },
        {
            "serial": 234567,
            "color": "black",
            "year": 2020,
        },
        {
            "serial": 345678,
            "color": "white",
            "year": 2012,
        }
    ]

    year = int(input("Year: "))
    print(list(filter(lambda x: x["year"] < year, car_list)))
    
"""
