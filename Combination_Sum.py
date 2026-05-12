from display import display

class Combination_Sum:
    def __init__(self, candidates, target):
        self.candidates = candidates
        self.target     = target

    @display("Combinations",header="Combinations Sum")
    def combinationSum(self):
        print(f"Candidates : {self.candidates}")    # ← print before result
        print(f"Target     : {self.target}")        # ← print before result
        result     = []
        candidates = sorted(set(self.candidates))

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()

        backtrack(0, [], self.target)
        return result if result else "No combination found"