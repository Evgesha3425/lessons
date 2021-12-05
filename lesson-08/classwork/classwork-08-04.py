"""
Оформить предыдущую задачу в виде программы, вынести функцию в отдельный файл, добавить
комментарии с описанием.
"""


from library import prime_numbers

if __name__ == "__main__":
    n = int(input("Enter N: "))
    m = int(input("Enter M: "))

    result = prime_numbers(n, m)
    print(result, len(result))