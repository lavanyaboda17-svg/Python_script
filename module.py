import bubble_sort
import quick_sort
import palindrome
import factorial
import sum_of_2_no
import sum_of_3_no
import sum_of_4_no
import water_example
import Combination_Sum
import median_task


if __name__ == "__main__":
    #bubble_sort
    arr = [5, 3, 8, 1, 9, 2]
    print(f"Before sorting: {arr}")
    bubble_sort.bubble_sort(arr) #call function
    print(f"After sorting: {arr}")

    #quick_sort
    arr = [5, 4, 8, 1, 9, 3]
    print(f"before sorting:,{arr}")
    result= quick_sort.quick_sort(arr)
    print(f"after sorting:{result}")
   

    #palindrome
    texts = ["madam","hello"]
    for text in texts:
        if palindrome.palindrome(text):
            print(text,"is a palindrome")
    else:
        print(text,"is not a palindrome")
        
             
    #factorial
    number = 3
    print(f"factorial is: {factorial.factorial(number)}") 


    #sum_of_2_no
    num = [1, 3]
    target = 9
    print(f"Numbers: {num}")
    print(f"Target: {target}")
    print(sum_of_2_no.two_sum(num, target))
   

    #sum_of_3_no
    nums = [-1, 0, 1, 2, -1, -4]
    num_1 = [-1.5, 0.5, 1.0, 2.0, -1.0, -0.5]
    print("three_sum: ", sum_of_3_no.threeSum(nums))
    print("three_sum: ", sum_of_3_no.threeSum(num_1))

    #sum_of_4_no
    nums     = [1, 0, -1, 0, -2, 2]
    num_1    = [2, 4, 5, 8, 2, 4]
    target   = 0
    target_1 = 12
    print("four_sum: ",sum_of_4_no.fourSum(nums, target)) 
    print("four_sum: ",sum_of_4_no.fourSum(num_1, target_1))

    #water_example
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Max Area: ",water_example.maxArea(height))  
    height_1 = [1, 2, -3, 4]
    print("Max Area: ",water_example.maxArea(height_1))
    height_2 = [0,0,0,0]
    print("Max Area: ",water_example.maxArea(height_2))
    height_3 = [-5,-3,-6,-2]
    print("Max Area: ",water_example.maxArea(height_3))
    height_4 = [3,7]
    print("Max Area: ",water_example.maxArea(height_4))
    height_5 = [3,7]
    print("Max Area: ",water_example.maxArea(height_5))

    #Combination_Sum
    candidates = [1,3,7,2,5]
    target = 5
    print("Combination of Sum:",Combination_Sum.combinationSum(candidates,target))

    #median_task
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    print("Normal Case  :", median_task.medianSortedArray(nums1, nums2)) 

    nums1 = [0, 0, 0]
    nums2 = [0, 0, 0]
    print("All Zeros    :", median_task.medianSortedArray(nums1, nums2))  

    nums1 = [-3, -1, 2]
    nums2 = [-2,  1, 4]
    print("Negative and Positive  :", median_task.medianSortedArray(nums1, nums2))  

    nums1 = [1, 3, 5]
    nums2 = []
    print("nums2 Empty  :", median_task.medianSortedArray(nums1, nums2))  

    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6]
    print("Different Sizes   :", median_task.medianSortedArray(nums1, nums2))  

    nums1 = [1]
    nums2 = [2]
    print("Single Each  :", median_task.medianSortedArray(nums1, nums2))
    
    nums1 = [-5, -3, -1]
    nums2 = [-4, -2,  -1]
    print("All Negative :", median_task.medianSortedArray(nums1, nums2)) 

    nums1 = [1, 3, 56, 100]
    nums2 = [2, 3, 4, 98]
    print("Repeated numbers :", median_task.medianSortedArray(nums1, nums2)) 






