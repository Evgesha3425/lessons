"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, в случае
положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""

"from manti-by"


import random


def get_card(used_cards):
    card_suit_list = ["H", "D", "C", "S"]
    card_list = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    while True:
        # Generate random suit
        index = random.randint(0, len(card_suit_list) - 1)
        card_suit = card_suit_list[index]

        # Generate random suit
        index = random.randint(0, len(card_list) - 1)
        card = card_list[index]

        current = f"{card_suit}-{card}"
        if current not in used_cards:
            return current


def get_card_sum(used_cards):
    card_values = {
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "D": 3, "K": 4, "A": 11
    }
    card_sum = 0
    for card in used_cards:
        key = card.split("-")[-1]
        card_sum += card_values[key]
    return card_sum


if __name__ == "__main__":
    cards = []
    while True:
        new_card = get_card(cards)
        cards.append(new_card)
        current_sum = get_card_sum(cards)
        print("Your cards:", cards)
        print("Current sum:", current_sum)

        if current_sum > 21:
            print("You've lost, game over.")
            break

        if current_sum == 21:
            print("You've almost won!")
            break

        choice = input("Do you want ot get the next card [Y/N]:")
        if choice == "N":
            break