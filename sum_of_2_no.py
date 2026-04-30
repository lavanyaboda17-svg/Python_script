#SUM OF TWO NUMBERS
def two_sum(num, target):
    seen = {}
    for i in range(len(num)):
        balance = target - num[i]
        if balance in seen:
            return seen[balance], i
        seen[num[i]] = i
    return "no pair found"
    
