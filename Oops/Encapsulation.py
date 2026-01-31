class BankAccount:
    def __init__(self,name,balance,deposit):
        self.name=name #public
        self._balance=balance #protected
        self.__deposit = deposit #privte data mangling
        
    def get_deposit(self):  #for accessing private data we use getter and setter method
        return self.__deposit

acc1=BankAccount("Sayan Pal", 100_000,25_000)

print(acc1.name, acc1._balance,acc1.get_deposit()) 
    