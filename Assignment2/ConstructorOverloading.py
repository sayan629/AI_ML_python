#| Q7. Create a class that allows the constructor to work with:                    |
#| • name only                                                                     |
#| • name + age                                                                    |
#| • name + age + address                                                          |
#| As direct constructor overloading (multiple constructors) are not allowed but   |
#| we have to use default parameters to simulate constructor overloading.          |
#__________________________________________________________________________________|


class Person:
    def __init__(self, name, age=None, address=None):
        self.name=name          # Store person's name
        self.age=age            # Store age (can be None)
        self.address=address    ## Store address (can be None)

p1=Person("Sayan")          # Creating object with only name
p2=Person("Samata",22)      # Creating object with name, age
p3=Person("Srinika",5,"West Bengal")    # Creating object with name, age and address


print(p1.__dict__)      # __dict__ shows all instance variables in dictionary form
print(p2.__dict__)
print(p3.__dict__)