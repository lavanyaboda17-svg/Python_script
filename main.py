# Bubble sorting
def bubble_sort(arr):
    for i in range(len(arr)): #3
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j] #swap
arr = list(map(int, input("Enter number(bubble_sort): ").split(",")))
print(f"Before sorting: {arr}")
bubble_sort(arr) #call function
print(f"After sorting: {arr}")


# Quick Sorting
def quick_sort(arr): 
    if len(arr) <= 1:      
        return arr
    pivot = arr[0]     #first item as pivot
    smaller = [x for x in arr[1:] if x <= pivot]   
    bigger  = [x for x in arr[1:] if x > pivot]    
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)
arr = [5, 3, 8, 1, 9, 2]
print(quick_sort(arr))  


#palindrome
def palindrome(word):
    if word == word[::-1]:
        return True
    return False
text = input("Enter string(palindrome): ")

if palindrome(text):
    print(text,"is a palindrome")
else:
    print(text,"is not a palindrome")


#factorial
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


#sum of two numbers
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


#sum of three numbers 
def threeSum(nums):
    n = len(nums) #n var to store count
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]] #putting in list
                    if triplet not in result:
                        result.append(triplet)
    return result
nums = [-1, 0, 1, 2, -1, -4]
       #[0, 1, 2, 3,  4,  5]
print("three sum:",threeSum(nums))

#sum of four numbers
def fourSum(nums, target):
    n = len(nums)
    result = []
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quad = [nums[i], nums[j], nums[k], nums[l]]
                        if quad not in result:
                            result.append(quad)
    return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
num_1 = [2,4,5,8,2,4]
target_1 = 12

print("four_sum:",fourSum(nums, target))
print("four_sum",fourSum(num_1, target_1))