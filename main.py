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



#palindrome
word = input("Enter String: ")
if word == word[::-1]:  #[::-1] reverse string == palindrome
        print(word, "is a Palindrome")
else:
    print(word, "is not a palindrome")
    
    
# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)  #calling itself
number = int(input("Enter number: "))
print(f"Factorial is: {factorial(number)}")