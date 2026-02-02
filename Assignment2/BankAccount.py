class BankAccount:
    def __init__(self,acc_number,owner_name,balance=0):
        self.acc_number=acc_number
        self.owner_name=owner_name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited: ",amount)
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")
    
    def check_balance(self):
        print("Current Balance:",self.balance)

acc = BankAccount(101, "Sayan", 5000)
acc.check_balance()
acc.deposit(2000)
acc.withdraw(1000)
acc.check_balance()