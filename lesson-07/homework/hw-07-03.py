"""
Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина. Каждая строка входного файла
представляет собой запись вида Покупатель, Товар, Количество, Стоимость где Покупатель - имя покупателя (строка
без пробелов), товар - название товара (строка без пробелов), количество - количество приобретенных единиц товара.
1. Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество
приобретенных им товаров и их стоимость.
2. Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее количество приобретенных
и их стоимость.
"""
from typing import Optional


def load_data_from_file(filename: Optional[str] = "shopping_list.txt") -> list:
    """Load data from file."""
    result = []
    db_file = open(filename, "r")
    for record in db_file.readlines():
        # Split records by comma
        record = record.split(",")

        # Cast values to integers
        record[2] = int(record[2])
        record[3] = int(record[3])

        # Save record to result
        result.append(record)
    return result


def get_stats(data: list, index: int = 0) -> dict:
    """ Generate list of users """
    result = {}
    for row in data:
        # If we already found user previously, aggregate new values
        if row[index] in result:
            result[row[index]]["products_bought"] += row[2]
            result[row[index]]["total_price"] += row[3]
        else:
            # Otherwise set initial values
            result[row[index]] = {
                "products_bought": row[2],
                "total_price": row[3],
            }
    return result


def main():
    """Main program function to get user's input and return result."""
    data = load_data_from_file()

    user_stats = get_stats(data)
    print("User stats: ", user_stats)

    product_stats = get_stats(data, index=1)
    print("Product stats: ", product_stats)


if __name__ == "__main__":
    main()