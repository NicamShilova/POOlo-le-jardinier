from Vegetable import Vegetable



class Carrot(Vegetable):
    def grow(self, number=0):
        self.value = number
    
    def seed(self, number=0):
        return self.value