from tr_cl_1 import Warrior


class Archer(Warrior):
    def __init__(self, stamina, health, arrows):
        super().__init__(health, stamina)
        self.arrows = arrows

    def introduces(self):
        super().introduces()
        print(f"\nArrows: {self.arrows}")
