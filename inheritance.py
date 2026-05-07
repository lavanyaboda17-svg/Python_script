class Food:  #parent class
    def cook(self):
        print("cooking food")
        
    def serve(self):
        print("serving food")
        
class pizza(Food): #child class 
    def topping(self):
        print("adding toppings")
        
p = pizza()

p.cook()
p.serve()

p.topping()