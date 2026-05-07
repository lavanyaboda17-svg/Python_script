class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def show(self):
        print(f"Name: {self.name},\nMarks: {self.marks}")
        
    def result(self):
        if self.marks >= 35:
            print(self.name,"passed")
        else:
            print(self.name,"failed")

s = Student("Alice",90)
s.show()
s.result()
        