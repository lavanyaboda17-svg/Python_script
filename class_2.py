class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hi i am {self.name}")
        print(f"my age is {self.age}")
        
p = person("lavanya",20)
p.greet()