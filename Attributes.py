class Student:
    University_name="KIIT-DU"  #This are the class Attributes
    
    def __init__(self, name, gpa):
        self.name=name              #Tihs are the Instances Attributes
        self.gpa=gpa

stu1  = Student("Sayan",8.7)

print(stu1.name)
print(stu1.University_name)
