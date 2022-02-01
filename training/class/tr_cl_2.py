from tr_cl_1 import Warrior, Mage


class Archer(Warrior):
    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows


unit1 = Archer()
unit2 = Archer()

print(unit1.__dict__)
unit1.introduces()
