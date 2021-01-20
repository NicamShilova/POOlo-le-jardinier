# from Vegetable import Vegetable
from Carrot import Carrot
from Corn import Corn
from Lettuce import Lettuce
    
carrot = Carrot()
# corn = Corn()
# lettuce = Lettuce()

class Garden():

    def __init__(self):
        self.p = []

    def add(self, veg):
        # veg.grow(8)
        # print(veg.seed())
        self.p.append(veg)
        print ("liste " + str(self.p))

    def _plant(self, cls=carrot):
        print (cls.__module__)


    # def _plant(self, cls=Tomato())