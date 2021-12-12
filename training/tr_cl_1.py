class Warrior:
    #перезаписал метод
    def __init__(self, stamina, health = 50):
        #поля
        self.__health = health
        self.stamina = stamina

    def _set_health(self, points):
        self.__health += points

    def introduces(self):
        print("-----------")
        print(f"Class: {self.__class__.__name__}")
        print(f"\nHealth: {self.__health}")
        print(f"\nStamina: {self.stamina}")

    def attacks(self, target):
        print("-----------")
        print(f"{self.__class__.__name__} attack {target.__class__.__name__}")
        target._set_health(-5)


unit1 = Warrior(100, 50)
unit2 = Warrior(80, 80)


class Mage:
    def __init__(self, mana, health = 50):
        self.mana = mana
        self.health = health

    def introduces(self):
        print("-----------")
        print(f"Class: {self.__class__.__name__}")
        print(f"\nHealth: {self.__health}")
        print(f"\nMana: {self.mana}")




unit1.attacks(unit2)
mage = Mage(40)
print(unit2.__health)