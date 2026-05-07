class Bank:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def show(self):
        print(f"Owner: {self.owner} \n Balance: {self.balance}")
    
    def deposit(self,amount):
        self.balance += amount
        print("New Balance",self.balance)
        
b = Bank("Alice",1000)

b.show()
b.deposit(500)
        
    