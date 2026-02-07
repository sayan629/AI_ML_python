#Design and Create an online Store for Products(name,price)
#Track total products being created.
#create a static method to calculatdiscount on each product based on a % parameter.

class Product:
    count=0  ## Class variable to store total product count
    
    # Constructor to initialize product details
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1
    
    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")
        
    @classmethod
    def get_count(cls):
        print(f"Total Products in Store= {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"Discounted Price = {price-(price*discount/100)}")

p1=Product("Phone", 10_000)
p2=Product("Laptop", 65_000)
p3=Product("Pen",10)

Product.get_count()
print()

p1.get_info()
p1.calc_discount(p1.price,12)
print()

p2.get_info()
p2.calc_discount(p2.price,40)
print()

p3.get_info()
p3.calc_discount(p3.price,1)
print()
