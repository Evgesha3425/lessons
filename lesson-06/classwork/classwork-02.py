"""
Доработать первое задание так, чтобы словарь читался из текстового
CSV файла, где на каждой строке пары слов вида: apple,яблоко.
"""


#ЧТО-то НЕ ПОЛУЧАЕТСЯ

import csv


def translate_en_to_ru(d, word):
    return d[word]


def translate_ru_to_en(d, word):
    for en, ru in d.items():
        if word == ru:
            return en


def load_dictionary():
    result = {}
    with open("dictionary.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            result[row[0]] = row[1]
    return result


if __name__ == "__main__":
    dictionary = load_dictionary()

    print(translate_en_to_ru(dictionary, "sun"))
    print(translate_ru_to_en(dictionary, "Луна"))