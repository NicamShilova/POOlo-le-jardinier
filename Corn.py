from Vegetable import Vegetable



class Corn(Vegetable):

    def __init__(self):
        self.value = 0

    def grow(self, number=0):
        self.value = number

    # def grow(self, valeur, number=0):
    #     # self.value = 0
    #     print ("valeur " + str(valeur))
    #     print ("number " + str(number))
    #     valeur += number
    #     self.value = valeur
    #     print ("self.value " + str(self.value))
    
    def seed(self, number=0):
        return self.value