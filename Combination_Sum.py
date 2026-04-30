#Combination Sum
def combinationSum(candidates, target):
    result = []
    
    def backtrack(start,current,remaining): #recursion 
        if remaining == 0:
            result.append(list(current))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()
    backtrack(0, [], target) 
    return result       
   
