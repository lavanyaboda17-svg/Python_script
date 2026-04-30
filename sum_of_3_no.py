#SUM OF THREE NUMBERS
def threeSum(nums):
    nums.sort()        # arrange from small to big
    n = len(nums)
    result = []

    for i in range(n - 2):                          # stop 2 before end
        if i > 0 and nums[i] == nums[i - 1]:        # skip duplicate i
            continue

        left  = i + 1                               # move left
        right = n - 1

        while left < right:        #keep gooing until pointers meet
            total = nums[i] + nums[left] + nums[right]  # add all 3 numbers
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left  += 1
                right -= 1
            elif total < 0:
                left  += 1                          # need larger number
            else:
                right -= 1                          # need smaller number

    return result


