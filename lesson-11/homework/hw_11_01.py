"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество,
комментарий. Реализовать следующие функции для продуктов: создание, чтение,
обновление по id, удаление по id.
"""

# В попытке сделать домашку запорол на самом начале:
# Не выходит создать файл product.sqlite3
import sqlite3


def create_products_table():
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                price INTEGER,
                count INTEGER,
                comment VARCHAR
            );
            """,
        )
        session.commit()


def create_products(name: str, price: int, count: int, comment: str):
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO products (name, price, count, comment)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, count, comment,),
        )
        session.commit()


if "name" == "__main__":
    create_products_table()
    create_products("milk", 20, 5, "Savushkin")
