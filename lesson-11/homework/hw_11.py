import sqlite3


# Создаем таблицу. Колонки таблицы указаны после CREAT TABLE products( ... )
def creat_table_products():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                price INTEGER,
                amount INTEGER,
                comment VARCHAR
            );
            """,
        )
        session.commit()


# Запуская ф-ию добавляем новый товар в таблицу
def add_product(name: str, price: int, amount: int, comment: str):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO products (name, price, amount, comment)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, amount, comment),
        )
        session.commit()


def show_products():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM products;
            """,
        )
        session.commit()
        return cursor.fetchall()


def update_amount():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE products
            SET amount = 250
            WHERE id = 4;
            """,
        )
        session.commit()
        return cursor.fetchone()


def delete_product():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM products
            WHERE id = 6;
            """,
        )
        session.commit()
        return cursor.fetchone()


if __name__ == "__main__":
    # Создаем таблицу products
    # creat_table_products()

    # Указываем сразу все аргументы, имеющиеся в функции. Сколько раз запустим, столько
    # раз и создаться новый товар с этими параметрами
    # add_product("Молоко", 25, 1250, "Савушкин")
    # add_product("Творог", 20, 900, "Брест-Литовск")
    # add_product("Хлеб", 20, 525, "Корона")
    # add_product("Колбаса", 75, 300, "Гродненский м-т")
    # add_product("Яйца", 40, 2000, "Молодецкие")
    # add_product("Ряженка", 35, 200, "Брест-Литовск")

    # Выводим все имеющиеся продукты из таблицы
    # leftovers = show_products()
    # print(leftovers)

    # Обновляем кличество оставшихся товаров по id продукта
    # update_amount()

    # Удаляем продукт из таблицы по id
     delete_product()
