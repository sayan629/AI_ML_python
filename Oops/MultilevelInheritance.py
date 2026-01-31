class Employee:
        start_time="9AM"
        end_time="10PM"
    
class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role

class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)  #using super we can invoke constructor of the parent class
        self.salary=salary

acc1= Accountant(25_0000,"CA")
print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time) 
        