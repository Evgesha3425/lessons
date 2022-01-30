import sqlite3

# Создаем таблицу. Колонки таблицы указаны после CREAT TABLE user( ... )
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


# Запуская ф-ию создается новый юзер
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


# Поиск по имени. В query(запрос) укажем имя по которому будем искать. Далее это имя
# попадет в поле WHERE firstname = ? . По этому параметру и будет осуществляться поиск
def search_user_name(query: str):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?;
            """,
            (query,),
        )
        session.commit()
        # В поле SELECT указываем какие столбцы хотим вывести.
        # В SELECT * выведет все имеющиеся в таблице столбцы
        # fetchall выведет всех найденных юзеров по имени
        # fetchone выведет первого найденного пользователя
        return cursor.fetchall()


def search_user_age(X: int, Y: int):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age > ? and age < ?;
            """,
            (X, Y,),
        )
        session.commit()
        return cursor.fetchall()


if __name__ == "__main__":

# Создадим пустую таблицу. После содания в директории рядом с файлом .py должен появиться
# файл db.sqlite3 . Имя этого файла указывали
# в функции в строке with sqlite3.connect("db.sqlite3") as session

    #create_user_table()


# Указываем сразу все аргументы, имеющиеся в функции. Сколько раз запустим, столько
# раз и создаться пользователь с этими параметрами

    # create_user("Evgeniy", "Pavlovich", "epavlovich@gmail.com", "jkl;k", 36)


# Поиск по имени.
# Выполненная ф-ия сделает return, поэтому присвоим функции имя и выведем его на печать

    # result_name = search_user_name("Evgeniy")
    # print(result_name)


# Поиск по возрасту

    result_age = search_user_age(60, 65)
    print(result_age)


