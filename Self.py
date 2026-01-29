class Student:
    def __init__(self,name,cgpa): #parameterized constructor
        self.name=name
        self.cgpa=cgpa
    
    def get_cgpa(self):
        return self.cgpa

stu1=Student("Sayan",9.22)   #creating Student Objects
stu2=Student("Ruhon",8.55)  
stu3=Student("Shlok",7.56)

# Command line outputs
print("----- Student Details -----")

print(f"{stu1.name} has CGPA = {stu1.get_cgpa()}")
print(f"{stu2.name} has CGPA = {stu2.get_cgpa()}")
print(f"{stu3.name} has CGPA = {stu3.get_cgpa()}")

print("---------------------------")
        