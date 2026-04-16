    
    
    # Palindrome using function
def palindrome(word):
    if word == word[::-1]:
        return True
    return False

text = input("Enter String: ")

if palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")
    
    
    
    # quick sorted
    
    
    def quick_sort(arr):
    if len(arr) <= 1:        # if 1 or 0 items, done!
        return arr

    pivot = arr[0]           # pick first item as pivot

    smaller = [x for x in arr[1:] if x <= pivot]   # items less than pivot
    bigger  = [x for x in arr[1:] if x > pivot]    # items greater than pivot

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


# Test
arr = [5, 3, 8, 1, 9, 2]
print(quick_sort(arr))   # [1, 2, 3, 5, 8, 9]