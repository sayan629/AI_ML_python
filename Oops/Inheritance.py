class Employee:   # Base class (Parent class)
    start_time="10Am"
    end_time="7pm"
    
    def change_time(self,new_end_time):
        self.end_time=new_end_time      # Creates instance variable for that object


# Derived class (Child class) - inherits Employee
class Teacher(Employee):  #Inheritance: 
    def __init__(self,subject):
        self.subject=subject


# Another derived class (Child class)
class AdminStaff(Employee):
    def __init__(self,Role):
        self.Role=Role

t1= Teacher("Python")
t2= AdminStaff("Clark")


# Changing end time only for t1
t1.change_time("6pm")

print (t1.subject, t1.start_time,t1.end_time ,t2.Role)   