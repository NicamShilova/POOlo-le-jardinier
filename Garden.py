# Importing extern classes
from Carrot import Carrot
from Corn import Corn
from Lettuce import Lettuce
    
carrot = Carrot()

test = 0

class Garden():

    # Initialisation
    def __init__(self):
        self.list = []
        self.count = 0

    # Initialising list of vegetables
    def add(self, veg):
        self.list.append(veg)
        self.count = len(self.list)

    # Detecting vegetable name
    def _plant(self, cls=carrot):
        return cls.__module__

    # Counting numbers of vegetables
    def counting(self, veg):
        return veg.seed()