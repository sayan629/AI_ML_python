#Method Overriding Example
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Car is driving....")

class Bike(Vehicle):
    def move(self):
        print ("Bike is riding...")

#Duck Typing Example

class Printer:
    def start(self):
        print("Printer Started...")

class Scanner:
    def start(self):
        print("Scanner Started...")

#Operator Overloading Example
class Number:
    def __init__(self,value):
        self.value=value
    
    def __add__(self,other):
        return self.value+other.value

print("\n=== Polymorphism using Method Overriding ===")
items=[Vehicle(),Car(),Bike()]
for i in items:
    i.move()

print("\n=== Polymorphism using Duck Typing ===")
devices=[Printer(),Scanner()]
for d in devices:
    d.start()

print("\n=== Polymorphism using Operator Overloading ===")
n1=Number(15)
n2=Number(25)
print("Sum= ", n1+n2)