from Vegetable import Vegetable



class Lettuce(Vegetable):
    def grow(self, valeur, number=0):
        valeur += number
        self.value = valeur
    
    def seed(self, number=0):
        return self.value