# Importing libraries
import random

# Importing extern classes
from Garden import Garden
from Carrot import Carrot
from Corn import Corn
from Lettuce import Lettuce
from Gardener import Gardener

# Declaring vegetables from factory
carrot = Gardener.Vege("Carrot")
corn = Gardener.Vege("Corn") 
lettuce = Gardener.Vege("Lettuce")

# Declaring garden
garden = Garden()

# Adding vegetables in the list
garden.add(carrot)
garden.add(corn)
garden.add(lettuce)

# Initialising variables
tour = 1
adding = 0
deduction = 0
total = 0
value = 0
nameVegetable = ""

#  Creating a loop which works until the max seed quantity (30) is detected
while (total < 30):
    
    adding = random.randint(1, 9)

    # Checking if it's max value is reached
    if (total + adding > 30):
        print ("Max capacity of garden reached")
        adding = adding - (total + adding - 30)

    # Each vegeatble get his adding
    if (tour == 1):
        carrot.grow(adding)
        nameVegetable = str(garden._plant(carrot))
        tour = 2
    elif (tour == 2):
        corn.grow(adding)
        nameVegetable = str(garden._plant(corn))
        tour = 3
    elif (tour == 3):
        lettuce.grow(adding)
        nameVegetable = str(garden._plant(lettuce))
        tour = 1

    # Display number of seeds added
    print("Added " + str(adding) + " seeds of " + str(nameVegetable))

    # Calculate total seeds for this garden and display result
    total = garden.counting(carrot) + garden.counting(corn) + garden.counting(lettuce)

    print(str(total) + " seeds for this garden")

# Display total vegetables in this garden and display result
print("Number of vegetables in this garden : " + str(garden.count))