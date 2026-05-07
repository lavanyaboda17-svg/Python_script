class Sum_of_three:
    def __init__(self, nums, target):
        self.nums   = nums
        self.target = target

    def threeSum(self):
        result = []
        nums   = sorted(self.nums)     # sort a copy, don't modify original
        n      = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:   # skip duplicates
                continue
            left  = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == self.target:
                    result.append([nums[i], nums[left], nums[right]])
                    left  += 1
                    right -= 1
                elif total < self.target:
                    left  += 1
                else:
                    right -= 1

        return result if result else "No triplet found"

    def display(self):
        print(f"Numbers : {self.nums}")
        print(f"Target  : {self.target}")
        print(f"Result  : {self.threeSum()}")