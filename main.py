from Garden import Garden
from Carrot import Carrot
from Corn import Corn
from Lettuce import Lettuce

carrot = Carrot() 
corn = Corn() 

garden = Garden() 
carrot.grow(8)
print(carrot)
garden.add(carrot)
corn.grow(8) 
garden.add(corn) 
# garden.add # display 8