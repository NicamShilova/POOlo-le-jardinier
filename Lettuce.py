# Importing extern classes
from Vegetable import Vegetable

class Lettuce(Vegetable):

    # Initialisation
    def __init__(self):
        self.value = 0

    # Adding seeds
    def grow(self, number=0):
        self.value += number
    
    # Get number of seeds
    def seed(self, number=0):
        return self.value