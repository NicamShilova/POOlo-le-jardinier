from Garden import Garden
from Carrot import Carrot
from Corn import Corn
from Lettuce import Lettuce
# from Jardinier import Jardinier



carrot = Carrot() 
corn = Corn() 
lettuce = Lettuce() 


  
# def Jardinier(self ="Carrot"): 

#     types = { 
#         "Carrot": Carrot, 
#         "Corn": Corn, 
#         "Lettuce": Lettuce, 
#     } 

#     return types[self]() 

# carrot = Jardinier("Carrot") 
# corn = Jardinier("Corn") 
# lettuce = Jardinier("Lettuce") 

# carrot = Jardinier.Vege("Carrot")
# corn = Jardinier.Vege("Corn") 
# lettuce = Jardinier.Vege("Lettuce")

valeur = 0

garden = Garden()  
carrot.grow(1)
carrot.grow(2)
# carrot.grow(0, 1)
# # garden.add(carrot)
# carrot.grow(carrot.seed(), 2)
garden.add(carrot)

garden = Garden() 
corn.grow(3)
corn.grow(4)
# corn.grow(0, 3)
# corn.grow(corn.seed(), 4)
garden.add(corn)

garden = Garden()  
lettuce.grow(5)
lettuce.grow(6)
# lettuce.grow(0, 5)
# lettuce.grow(lettuce.seed(), 6)
garden.add(lettuce)

garden._plant(carrot) 
print(carrot.seed())
garden._plant(corn) 
print(corn.seed())
garden._plant(lettuce) 
print(lettuce.seed())

# garden = Garden() 
# carrot.grow(8)
# # print(carrot)
# garden.add(carrot)
 
# # garden.add(corn) 
# corn.grow(valeur, 8)
# valeur = corn.seed()
# print ("valeur1 " + str(valeur))
# garden._plant(corn) 

# corn.grow(valeur, 4) 
# garden.add(corn) 
# valeur = corn.seed()
# print ("valeur2 " + str(valeur))

# print(valeur)
# garden.add # display 8