class BankAccount:
    def __init__(self,name,balance,deposit):
        self.name=name #public
        self._balance=balance #protected
        self.__deposit = deposit #privte data mangling
        
    def get_deposit(self):  #for accessing private data we use getter and setter method
        return self.__deposit
    
    def set_deposit(self,new_deposit): #setter 
        self.__deposit=new_deposit

acc1=BankAccount("Sayan Pal", 100_000,25_000)
acc1.set_deposit(20_000)

print(acc1.name, acc1._balance,acc1.get_deposit()) 
    