"""
Создать функцию, которая создает таблицу user, для примера использовать слайд №12.
Запустить функцию и проверить, что создался файл базы данных.
"""

"""
Создать функцию, которая позволяет добавлять данные 
в таблицу user. Добавить 5 различных записей.
"""

"""
Создать функцию для поиска всех пользователей с определенным именем. 
Запустить функцию и найти хотя бы одного пользователя по имени.
"""

import sqlite3


def create_user_table():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname VARCHAR,
                lastname VARCHAR,
                email VARCHAR,
                password VARCHAR,
                age INTEGER,
                datetime DATETIME
            );
            """,
        )
        session.commit()


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()


def search_user(query: str):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT firstname, lastname, age 
            FROM user 
            WHERE firstname = ? 
            """,
            (query,),
        )
        session.commit()
        return cursor.fetchone()


if __name__ == "__main__":
    """
    create_user("Evgeniy", "Eidelman", "yauheni.skills@gmail.com", "Pass", 24)
    create_user("Anatoliy", "Eidelman", "aie@tut.by", "MyPass", 64)
    create_user("Artsiom", "Martunenka", "amartynenka@kan-therm.com", "MyNewPass", 24)
    create_user("Anna", "Kolos", "kolos.ann@mail.ru", "PassWord", 25)
    create_user("Kirill", "Barankevich", "kubik12@gmail.com", "NewPassword", 23)
    """
    result = search_user("Anna")
    print(result)