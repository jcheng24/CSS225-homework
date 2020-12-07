import random

#map
class Item:
    name = ""
    x = "0"
    y = "0"

    def __init__(self,new_name):
        self.name = new_name
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)


