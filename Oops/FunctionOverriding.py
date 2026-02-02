class Employee:
    def get_designation(self):          #parent class
        print("designation=Employee") 

class Teacher(Employee):       #child class
    def get_designation(self):
        print("designation=Teacher")   #function Overriding => Redfining parent class function in child classes.

t1= Teacher()
t1.get_designation() 