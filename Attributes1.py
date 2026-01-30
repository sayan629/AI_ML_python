class Student:
    University_name="KIIT-DU"  #This are the class Attributes
    PI=3.1
    def __init__(self, name, gpa):
        self.name=name              #Tihs are the Instances Attributes
        self.gpa=gpa
        self.PI=3.14

stu1  = Student("Sayan",8.7)

print(stu1.name)
print(stu1.University_name)
print(stu1.PI) #Here it would print Instance attributes
                #because if we have same attributes then always Instance attributes have higher priority
