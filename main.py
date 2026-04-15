# Bubble sorting
arr = [100,80,50,2,4]
for i in range(len(arr)):
    for j in range(len(arr)-1):
       if arr[j] > arr[j+1]:
           arr[j] , arr[j+1] = arr[j+1] , arr[j] #swap
print("Before sorting array:",arr)
print("After sorting array:" ,arr)

# Quick Sorting



#palindrome
word = input("Enter String: ")
if word == word[::-1]:
        print(word, "is a Palindrome")
else:
    print(word, "is not a palindrome")
    
    
# Factorial

number = int(input("Enter a number: "))
result = 1
for i in range (1,number + 1):
    result = result * i
print(f"Factorial of {number} is",result)