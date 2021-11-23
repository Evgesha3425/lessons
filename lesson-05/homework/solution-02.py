"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие
записки с именами участников. Затем каждый играющий по очереди вытягивает бумажку
с именем того, кому предстоит вручить презент. Ваша программа должна используя список
имен участников выдать на выходе пары, кто и кому будет дарить, причем сам себе человек
не может подарить, дубликаты тоже не допустимы.
"""

# Не понял что значит "дубликаты не допустимы"
# Не написано что нужно реализовать алгоритм с помощью def, поэтому пошел по пути наименьшего сопротивления

import random
names_donates = ["Alex", "Ivan", "Dmitriy", "Daria", "Ekaterina", "Roman"]    # игроки которые дарят подарок
names_get = ["Alex", "Ivan", "Dmitriy", "Daria", "Ekaterina", "Roman"]    # игроки которые получают подарок
for i in range(6):    # сколько игроков, столько и итераций
    rand = random.choice(names_get)
    if names_donates[i] == rand:    # найду человека которому буду дарить
        while names_donates[i] == rand:    # чтобы не вытянул сам себя
            rand = random.choice(names_get)
        print(f"{names_donates[i]} дарит подарок {rand}")
        names_get.remove(rand)    # того кого вытянули удаляем из игры
    else:
        print(f"{names_donates[i]} дарит подарок {rand}")
        names_get.remove(rand)    # того кого вытянули удаляем из игры






