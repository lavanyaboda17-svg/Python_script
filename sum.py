from display import display

class SubsetSum:
    def __init__(self, nums, target):
        self.nums   = nums
        self.target = target

    @display("Pair",header="Two Sum")
    def two_sum(self):
        print(f"Numbers : {self.nums}")        # ← print before result
        print(f"Target  : {self.target}")      # ← print before result
        seen = {}
        for num in self.nums:
            balance = self.target - num
            if balance in seen:
                return [balance, num]
            seen[num] = True
        return "No pair found"

    @display("Triplet",header="Three Sum")
    def three_sum(self):
        print(f"Numbers : {self.nums}")        # ← print before result
        print(f"Target  : {self.target}")      # ← print before result
        result = []
        nums   = sorted(self.nums)
        n      = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == self.target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1; right -= 1
                elif total < self.target:
                    left  += 1
                else:
                    right -= 1
        return result if result else "No triplet found"

    @display("Quadruplet",header="Four Sum")
    def four_sum(self):
        print(f"Numbers : {self.nums}")        # ← print before result
        print(f"Target  : {self.target}")      # ← print before result
        result = []
        nums   = sorted(self.nums)
        n      = len(nums)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == self.target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1; right -= 1
                    elif total < self.target:
                        left  += 1
                    else:
                        right -= 1
        return result if result else "No quadruplet found"