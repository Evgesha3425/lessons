"""
Написать функцию которая возвращают случайным образом одну карту из
стандартной колоды в 36 карт, где на первом месте номинал карты
номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""


import random


def pull_the_card(d, s):
    heart_den = {}    # колода черви
    diamonds_den = {}    # колода бубны
    clubs_den = {}    # колода трефы
    spades_den = {}    # колода пики
    deck_of_cards = [heart_den, diamonds_den, clubs_den, spades_den]
    card_random = random.choice(deck_of_cards)


    for i in range(4):
        for denomination in cards_denomination:
            if i == 0:
                heart_den[denomination] = [card_suit[i]]
            if i == 1:
                diamonds_den[denomination] = [card_suit[i]]
            if i == 2:
                clubs_den[denomination] = [card_suit[i]]
            if i == 3:
                spades_den[denomination] = [card_suit[i]]


    denomination, suit = random.choice(list(card_random.items()))
    print(denomination, suit)


if __name__ == "__main__":
    cards_denomination = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                          "J": 2, "D": 3, "K": 4, "A": 11}  # номинал карт
    card_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]  # масть карт
    pull_the_card(cards_denomination, card_suit)