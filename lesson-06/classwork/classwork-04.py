"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается,
достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.

"""

# Не получилось


import random


def pull_the_card(d, s):
    heart_den = {}  # колода черви
    diamonds_den = {}  # колода бубны
    clubs_den = {}  # колода трефы
    spades_den = {}  # колода пики
    deck_of_cards = [heart_den, diamonds_den, clubs_den, spades_den]
    card_random = random.choice(deck_of_cards)  # засунули в список чтобы случайным образом доставать карту

    number = 0
    for i in range(4):  # распихиваем наши карты по словарям
        for denomination in cards_denomination:
            if i == 0:
                heart_den[denomination] = [card_suit[i]]
            if i == 1:
                diamonds_den[denomination] = [card_suit[i]]
            if i == 2:
                clubs_den[denomination] = [card_suit[i]]
            if i == 3:
                spades_den[denomination] = [card_suit[i]]

    random.choice(list(card_random.items()))
    return d[random.choice(list(card_random.items()))[0]]




if __name__ == "__main__":
    cards_denomination = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                          "J": 2, "D": 3, "K": 4, "A": 11}  # номинал карт
    card_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]  # масть карт
    pull_the_card(cards_denomination, card_suit)


sum = 0
my_ask = input("Будешь тянуть карту? (yes/no): ")
if my_ask == "yes":
    sum += pull_the_card(cards_denomination, card_suit)


