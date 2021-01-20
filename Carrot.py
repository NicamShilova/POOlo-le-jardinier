from Vegetable import Vegetable



class Carrot(Vegetable):

    def __init__(self):
        self.value = 0

    def grow(self, number=0):
        self.value += number

    # def grow(self, number=0):
        
    #     valeur += number
    #     self.value = valeur
    
    def seed(self, number=0):
        return self.value