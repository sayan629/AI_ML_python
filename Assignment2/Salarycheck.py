# Q6. Create an abstract class with an abstract method
# calculate_salary().
# Create subclasses Intern, FullTimeEmployee and Contract Employee that
# implement the method differently.

from abc import ABC, abstractmethod

# Employee is an abstract class
# It defines a common structure for all employee types
class Employee(ABC):
    def calculate_salary(self):
        pass                     # No implementation here

# Abstract method
# Every child class MUST implement this method
@abstractmethod 

class Intern(Employee):    # Intern class inherits from Employee
    def calculate_salary(self):
        return 2000

class FullTime(Employee):
    def calculate_salary(self):
        return 7000

class Contract(Employee):
    def calculate_salary(self):
        return 5000

# Creating object of FullTime class
# Cannot create object of Employee because it is abstract
e1=Intern()
e2=FullTime()
e3=Contract()

# Calling overridden method
print(e1.calculate_salary())
print(e2.calculate_salary())
print(e3.calculate_salary())
