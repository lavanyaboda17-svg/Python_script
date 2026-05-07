class Locker:
    def __init__(self,password):
        self.__password = password #hidden
        
    def get_password(self):
        print("password",self.__password)
        
    def set_password(self,new):
        self.__password = new
        print("password updated")
        
l =Locker(1234)

l.get_password()
l.set_password(5678)

l.get_password() 
        
        
# Start
#   ↓
# l = Locker(1234)        → object created, password = 1234 🔒
#   ↓
# l.get_password()        → prints Password: 1234
#   ↓
# l.set_password(5678)    → password changed to 5678
#   ↓
# l.get_password()        → prints Password: 5678
#   ↓
# End