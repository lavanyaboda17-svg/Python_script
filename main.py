# Bubble sorting
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
arr = list(map(int, input("Enter number: ").split(",")))
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
text = input("Enter string: ")

if palindrome(text):
    print(text,"is a palindrome")
else:
    print(text,"is not a palindrome")
        
    
    
# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)  #calling itself
number = int(input("Enter number: "))
print(f"Factorial is: {factorial(number)}")