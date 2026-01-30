class Laptop:
    storage_type="ssd"
    
    def __init__ (self,RAM,storage):
        self.RAM=RAM
        self.storage=storage
    
    @classmethod  #decorator of the class Metod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")
    
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")
    
    @staticmethod  #decorator of the Static Metod
    def calc_discount(price, discount):
        final_price=price-(discount*price/100)
        print(f"Discounted price ={final_price}")
        
l1=Laptop("16gb" ,"512gb")
l1.calc_discount(40_000,10) #We can write intger in this type also to represent big number of integer value.