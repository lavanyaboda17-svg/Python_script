#SUM OF FOUR NUMBERS
def fourSum(nums, target):
    nums.sort() #arrange from small to big
    n = len(nums)
    result = [] 
    for i in range(n - 3): #stop 3 before end 
        if i > 0 and nums[i] == nums[i-1]: #0,0 skip one zero 
            continue 
        for j in range(i + 1, n - 2): # n-2 because we need space for left, right
            if j > i + 1 and nums[j] == nums[j-1]: #avoid duplicate 
                continue
            left  = j + 1  #move left
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right] #add all 4 numbers
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left  += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result

