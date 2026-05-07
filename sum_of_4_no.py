class sum_of_four:
    def __init__(self, nums, target):
        self.nums   = nums
        self.target = target

    def fourSum(self):
        result = []
        nums   = sorted(self.nums)    # sort a copy, don't modify original
        n      = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:          # skip duplicates
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # skip duplicates
                    continue
                left  = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == self.target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left  += 1
                        right -= 1
                        while left < right and nums[left]  == nums[left  - 1]:
                            left  += 1                     # skip duplicates
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1                     # skip duplicates
                    elif total < self.target:
                        left  += 1
                    else:
                        right -= 1

        return result if result else "No quadruplet found"

    def display(self):
        print(f"Numbers : {self.nums}")
        print(f"Target  : {self.target}")
        print(f"Result  : {self.fourSum()}")