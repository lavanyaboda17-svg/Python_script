class Sum_of_Two:
    def __init__(self, num, target):
        self.num    = num
        self.target = target

    def two_sum(self):
        seen = {}
        for i in range(len(self.num)):
            balance = self.target - self.num[i]   # what we need to find
            if balance in seen:
                return (seen[balance], i)          # return index pair
            seen[self.num[i]] = i                  # store index of current
        return "No pair found"

    def display(self):
        result = self.two_sum()
        print(f"Numbers : {self.num}")
        print(f"Target  : {self.target}")
        print(f"Result  : {result}")