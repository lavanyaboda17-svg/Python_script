#BUBBLE SORTING
def bubble_sort(arr):
    for i in range(len(arr)): #3
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j] #swap
arr = list(map(int, input("Enter number(bubble_sort): ").split(",")))
print(f"Before sorting: {arr}")
bubble_sort(arr) #call function
print(f"After sorting: {arr}")


#QUICK SORTING
def quick_sort(arr): 
    if len(arr) <= 1:      
        return arr
    pivot = arr[0]     #first item as pivot
    smaller = [x for x in arr[1:] if x <= pivot]   
    bigger  = [x for x in arr[1:] if x > pivot]    
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)
arr = [5, 3, 8, 1, 9, 2]
print(quick_sort(arr))  


#PALINDROME
def palindrome(word):
    if word == word[::-1]:
        return True
    return False
text = input("Enter string(palindrome): ")

if palindrome(text):
    print(text,"is a palindrome")
else:
    print(text,"is not a palindrome")


#FACTORIAL
def factorial(n):
    if n < 0:
        print("negative number don't have factorial")
        return
    elif n != int(n):
        print("Decimal number don't have factorial")
        return
    elif n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
    
number = int(input("enter number(factorial): "))
print(f"factorial is: {factorial(number)}")


#SUM OF TWO NUMBERS
def two_sum(num, target):
    seen = {}
    for i in range(len(num)):
        balance = target - num[i]
        if balance in seen:
            return seen[balance], i
        seen[num[i]] = i
        return "no pair found"
    
num = list(map(int, input("Enter numbers(sum of two num): ").split()))
target = int(input("Enter target: "))
print(two_sum(num, target))


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

nums = [-1, 0, 1, 2, -1, -4]
num_1 = [-1.5, 0.5, 1.0, 2.0, -1.0, -0.5]
print("three_sum: ", threeSum(nums))
print("three_sum: ", threeSum(num_1))


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

nums     = [1, 0, -1, 0, -2, 2]
num_1    = [2, 4, 5, 8, 2, 4]
target   = 0
target_1 = 12

print("four_sum: ",fourSum(nums, target)) 
print("four_sum: ",fourSum(num_1, target_1))
 
#WATER EXAMPLE
def maxArea(height):
    length_of_height= len(height)
    if length_of_height == [1,0] or all(h <= 0 for h in height):
        return 0
    if length_of_height == 2:
        area = min(height[0], height[1]) * 1
        print("Only 2 walls area is :",area)     #(maxArea([3, 7])) = 3
        return area  
    left, right = 0,length_of_height - 1   # 9-1 = 8
    max_water = 0 
    while left < right:
        # Calculate current area
        width = right - left #left=1, right=8 → width = 8-1 = 7
        current_area = min(height[left], height[right]) * width
        max_water = max(max_water, current_area)
         # Move the pointer with the shorter height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

# Test
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Max Area: ",maxArea(height))  
height_1 = [1, 2, -3, 4]
print("Max Area: ",maxArea(height_1))
height_2 = [0,0,0,0]
print("Max Area: ",maxArea(height_2))
height_3 = [-5,-3,-6,-2]
print("Max Area: ",maxArea(height_3))
height_4 = [3,7]
print("Max Area: ",maxArea(height_4))
height_5 = [3,7]
print("Max Area: ",maxArea(height_5))

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
   
candidates = [1,3,7,2,5]
target = 5
print("Combination of Sum:",combinationSum(candidates,target))


#median task
def medianSortedArray(nums1, nums2):
    i, j = 0, 0
    total = len(nums1) + len(nums2)
    mid = total // 2
    prev, curr = 0, 0

    for _ in range(mid + 1): #(1,2,3/ 0,1,2,3 index)
        prev = curr
        if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    if total % 2 == 1:
        return float(curr)
    else:
        return (prev + curr) / 2.0

# Test
nums1 = [1, 3, 5]
nums2 = []
print("Median:", medianSortedArray(nums1, nums2))  