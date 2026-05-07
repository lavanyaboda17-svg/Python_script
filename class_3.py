class cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    def meow(self):
        print(f"i am {self.name} and i am {self.color}")
    
c = cat("tommy","black")
c.meow()
        