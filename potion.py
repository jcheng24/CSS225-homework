import random

class Potion:
    name = ""
    effect = ""
    time = 0

    def __init__(self, new_name):
        self.name = new_name

        #self.effect = effect

        self.time = random.randint(5,10)
