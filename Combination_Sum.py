class Combination_Sum:
    def __init__(self, candidates, target):
        self.candidates = candidates
        self.target     = target

    def combinationSum(self):
        result     = []
        candidates = sorted(set(self.candidates))

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return
            if remaining < 0:
                return
            if len(result) >= 10:
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()

        backtrack(0, [], self.target)
        return result if result else "No combination found"

    def display(self):
        print(f"Candidates : {self.candidates}")
        print(f"Target     : {self.target}")
        result = self.combinationSum()
        if isinstance(result, list):
            print(f"Result     : {len(result)} combinations found")
            for combo in result:
                print(f"             {combo}")
        else:
            print(f"Result     : {result}")