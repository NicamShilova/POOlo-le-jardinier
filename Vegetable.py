from abc import ABC, abstractmethod
# from Carrot import Carrot
 
class Vegetable(ABC):
 
    def __init__(self):
        # self.value = value
        super().__init__()
    
    # @abstractmethod
    # def Carrot(self):
    #     pass
    
    # @abstractmethod
    # def Corn(self):
    #     pass
    
    # @abstractmethod
    # def Lettuce(self):
    #     pass

    @abstractmethod
    def grow(self):
        pass

# carotte = Carrot()
# carotte.grow(8)