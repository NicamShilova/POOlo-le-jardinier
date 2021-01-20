from Carrot import Carrot
from Corn import Corn
from Lettuce import Lettuce

carrot = Carrot()
corn = Corn()
lettuce = Lettuce()

class Jardinier():

    def __init__(self, types): 
        self.types = {}
    

    @staticmethod
    def Vege(selection):
        """
        docstring
        """
        types = { 
            "Carrot": carrot, 
            "Corn": corn, 
            "Lettuce": lettuce, 
        } 

        return types[selection]