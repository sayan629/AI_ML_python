from abc import ABC, abstractmethod #ABC-> Abstraction classes
class Animal(ABC):
    @abstractmethod  #a class that was not implemented we called basically abstract method for decoration we use abstractmethod in the top.
    def make_sound(self):   
        pass   # pass used when we does not want implementation in that class.

            
class Lion(Animal):
    def make_sound(self):
        print("Roar!")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo!!")

lion= Lion()
lion.make_sound()

cow=Cow()
cow.make_sound() 
