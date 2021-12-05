"""
Используя рекурсивную функцию вывести в порядке возрастания все простые числа,
расположенные между n и m (включая сами числа n и m), а также количество x этих чисел.
"""


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


if __name__ == "__main__":
    n = int(input("Enter N: "))
    m = int(input("Enter M: "))

    result = prime_numbers(n, m)
    print(result, len(result))