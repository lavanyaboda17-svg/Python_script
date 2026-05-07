class dog:
    def __init__(self,name,age): #self : refers current object
        self.name = name
        self.age = age
        
    def bark(self):
        print("Woof!")
            
    def show(self):
        print(f"Name:{self.name}, Age: {self.age}")
        
d = dog("sweety",3)
d.bark()
d.show()