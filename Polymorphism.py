class Vehical:   #parent class
    def move(self): #move base class 
        print("Moving..")
    
class car(Vehical):  #child class
   def move(self):
            print("car drives on road")
            
class boat(Vehical):
     def move(self):
         print("boat sails on water")   
        
class plan(Vehical):
    def move(self):
        print("plan files in sky")
        
c = car()
b = boat()
p = plan()


c.move()
b.move()
p.move()