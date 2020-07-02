from Snake import Snake

class Python(Snake):

    def __init__(self, large, two_lungs, venom):
        self.large = large
        self.two_lungs = two_lungs
        self.venom = venom

    def digest_large_prey(self):
        pass

    def constrict(self):
        pass

    def climb(self):
        pass

    def shed_skin(self):
        pass

obj1 = Python(True, False, False)
print(obj1.hunt())