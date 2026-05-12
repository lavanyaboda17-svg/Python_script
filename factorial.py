from display import display

class Factorial:
    def __init__(self, n):
        self.n = n

    @display("Factorial",header="Factorial")
    def factorial(self):
        print(f"Number : {self.n}")             # ← print before result
        n = self.n
        if n < 0:
            return "Negative numbers don't have factorials"
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result