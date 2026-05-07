class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def show(self):
        print(f"Brand : {self.brand}")
        print(f"price : {self.price}")
        
m = Mobile("Samsung",15000)
m.show()