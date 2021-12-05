CAR_LIST = [
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


def filter_cars(car_list: list, year: int) -> list:
    """Filter cars by year"""
    result = []
    for car in car_list:
        if car["year"] < year:
            result.append(car)
    return result


def prime_numbers(n: int, m: int) -> list:
    result = []
    for element in range(n, m + 1):
        is_prime = True
        for divider in range(2, element):
            if divider > 1 and element % divider == 0:
                is_prime = False
                break
        if is_prime:
            result.append(element)
    return result
