#| Q9. Create the following classes: Herbivore , Carnivore , omnivore with some     |
#| attributes & methods. Then create a class Bear that inherits from all the above  |   
#| classes to showcase how multiple inheritance works.                              |
#|__________________________________________________________________________________|



# Herbivore class Represents animals that eat plants
class Herbivore:
    def food(self):
        print("Eats Plant.....")


# Carnivore class Represents animals that eat meat
class Carnivore():
    def food2(self):
        print("Eats Meat...")
        
        
# Omnivore class Represents animals that eat both plants and meat
class Omnivore():
    def food3(self):
        print("Eats Both (Meat & Plant)")
        
        
# Bear class inherits from Herbivore, Carnivore, and Omnivore, This demonstrates multiple inheritance
class Bear(Herbivore,Carnivore,Omnivore):
    pass


b=Bear()  # Creating object of Bear class

# Calling methods from all parent classes
b.food()
b.food2()
b.food3()
