"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее
число подряд идущих элементов этой последовательности равны друг другу и что это за элемент.
Т.е. если программе на вход подать последовательность [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5],
то на печать программа должна вывести числа 4 и 3, где 4 - повторяющийся элемент, 3 - количество повторений
"""


def repeating_element(my_new_list: list) -> dict:
    #пустой словарь, в который занесем ключи, либо увеличим значения, если ключ уже имеется
    my_dict = {}
    #при появлении нового элемента его значение n = 1
    n = 1

    for i in my_new_list:
        if i not in my_dict:
            my_dict[i] = n
        else:
            my_dict[i] += 1

    #переберем ключи, найдя наибольший
    my_new_dict = {}
    x = 0

    for key, value in my_dict.items():
        if value > x:
            my_new_dict.clear()
            my_new_dict[key] = value

    print(my_new_dict)


if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5]
    my_new_list = []

    for i in my_list:
        if i != 0:
            my_new_list.append(i)
        else:
            break

    repeating_element(my_new_list)
