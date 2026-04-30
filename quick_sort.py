#QUICK SORTING
def quick_sort(arr): 
    if len(arr) <= 1:      
        return arr
    pivot = arr[0]     #first item as pivot
    smaller = [x for x in arr[1:] if x <= pivot]   
    bigger  = [x for x in arr[1:] if x > pivot]    
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)
 
