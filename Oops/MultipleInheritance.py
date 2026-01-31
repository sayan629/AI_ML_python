class Teacher:
    def __init__(self,salary):
        self.salary=salary
        
class Student:
    def __init__(self,gpa):
        self.gpa=gpa

class TA(Teacher,Student):   #Multiple Inheritance
    def __init__(self, salary,gpa,name):
        super().__init__(salary) # if we call from super then we need not write self
        Student.__init__(self,gpa) #but in case if we call using  class name then we need self
        self.name=name

ta1=TA(15_000,9.33, "Sayan Pal")

print(ta1.name, ta1.gpa, ta1.salary)