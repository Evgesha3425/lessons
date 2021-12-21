"""
Создать программу позволяющую осуществлять поиск по имени или возрасту,
оба параметра вводятся с клавиатуры.
"""
import sqlite3


#Поиск по возрасту
def search_user_age(number: int):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT firstname, lastname, age 
            FROM user 
            WHERE age = ?
            """,
            (number,),
        )
        session.commit()
        return cursor.fetchall()


def search_user(name: str):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT firstname, lastname, age 
            FROM user 
            WHERE firstname = ? 
            """,
            (name,),
        )
        session.commit()
        return cursor.fetchall()


if __name__ == "__main__":
    my_string = input("Enter first name or age: ")
    if my_string is str:
        result = search_user(int[my_string])
        print(result)

    if my_string is int:
        result = search_user_age(my_string)
        print(result)

