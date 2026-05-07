from abc import ABC, abstractmethod  #abc:specail module ABC → makes class 
                                     #abstract abstractmethod → makes method abstract

class Fodd (ABC):
    @abstractmethod
    def order (self):
        pass
    
class pizza(Fodd):
    def order(self):
        print("pizza is  ordered")
        
class burger(Fodd):
    def order(self):
        print("burger is ordered")
        
class biryani(Fodd):
    def order(self):
        print("biryani is ordered")
        
p = pizza()
b = burger()
bi = biryani()

p.order()
b.order()
bi.order()