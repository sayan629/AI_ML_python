# Q3. Create a class with private attributes _name,_roll_no, and _marks.
# Provide getter and setter methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 &100&name cannot be empty).

class Student:
    def __init__(self,name,roll,marks):
        self.set_name(name)
        self.set_roll(roll)
        self.set_marks(marks)
    
    def set_name(self,name):
        if name !='':
            self.name=name
    
    def set_roll(self,roll):
        if 1<=roll<=100:
            self.roll=roll
    
    def set_marks(self,marks):
        if marks>=0:
            self.marks=marks
            
    def get_details(self):
        return self.name, self.roll, self.marks

s=Student("Amit",5,100)
s1=Student("Sayan",1,10)
print(s.get_details())
print(s1.get_details())