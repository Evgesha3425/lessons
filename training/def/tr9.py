"""
Дано действительное положительное число a и целоe число n.
Вычислите a**n. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
"""


def power(a, n):
    result = 1

    for _ in range(abs(int(n))):
        if n >= 0:
            result = result * a

        else:
            result = result * (1 / a)

    return result


a = float(input("Enter a: "))
n = float(input("Enter n: "))
print(power(a, n))
