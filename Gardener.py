# Importing extern classes
from Carrot import Carrot
from Corn import Corn
from Lettuce import Lettuce

# Declaring vegetables
carrot = Carrot()
corn = Corn()
lettuce = Lettuce()

class Gardener():

    # Initialisation
    def __init__(self, types): 
        self.types = {}
    
    # Declaring factory
    @staticmethod
    def Vege(selection):
        types = { 
            "Carrot": carrot, 
            "Corn": corn, 
            "Lettuce": lettuce, 
        } 

        return types[selection]