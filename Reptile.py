from Animal import Animal

class Reptile(Animal):

    def __init__(self, alive, eyes,cold_blooded, tetrapod, heart_chambers, amniotic_eggs):
        super().__init__(alive, eyes)
        self.cold_blooded = cold_blooded
        self.tetrapod = tetrapod
        self.heart_chambers = heart_chambers
        self.amniotic_eggs = amniotic_eggs

    def seek_heat(self):
        pass

    def hunt(self):
        pass

    def use_venom(self):
        pass

    def attract_mate_through_scent(self):
        pass

max = Reptile(True, 2, False, False, 2, False)

print(max.heart_chambers)