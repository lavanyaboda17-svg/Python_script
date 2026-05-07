class Factorial:
    def __init__(self, n):
        self.n = n

    def factorial(self, n):
        if n < 0:
            return " Negative numbers don't have factorials"
        elif n != int(n):
            return " Decimal numbers don't have factorials"
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)   # recursive call

    def display(self):
        result = self.factorial(self.n)
        print(f"factorial({self.n}) = {result}")