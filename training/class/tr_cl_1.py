class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    def introduces(self):
        print('------------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHelath: {self.health}',
              f'\nStamina: {self.stamina}')
        print('------------------')

    def heals(self, target):
        print('------------------')
        print(f'{self.__class__.__name__} накладывает повязку из целебных трав {target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровьe у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
        print('------------------')

    def attacks(self, target):
        print('------------------')
        print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровьe у {target.__class__.__name__} понижено до {target.health}')
        print('------------------')

"""
unit1 = Warrior(stamina=100, health=100)
unit2 = Warrior(health=85, stamina=110)
"""

class Mage:
    def __init__(self, health=60, mana=100):
        self.health = health
        self.mana = mana

    def introduces(self):
        print('------------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHelath: {self.health}',
              f'\nStamina: {self.mana}')
        print('------------------')

    def heals(self, target):
        print('------------------')
        print(f'{self.__class__.__name__} применяет заклинание лечения',
              f'к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровьe у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.mana} единиц магии')
        print('------------------')

    def attacks(self, target):
        print('------------------')
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровьe у {target.__class__.__name__} понижено до {target.health}')
        print('------------------')

"""
unit3 = Mage()
unit4 = Mage(health=50, mana=110)


unit1.attacks(unit3)
unit4.attacks(unit2)
"""