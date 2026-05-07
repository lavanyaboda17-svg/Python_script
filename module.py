from bubble_sort import BubbleSort
from quick_sort import QuickSort
from palindrome import Palindrome
from factorial import Factorial
from sum_of_2_no import Sum_of_Two
from sum_of_3_no import Sum_of_three
from sum_of_4_no import sum_of_four
from water_example import MaxWater
from Combination_Sum import Combination_Sum
from median_task import MedianSorted
from sort import Sort


if __name__ == "__main__":

    # bubble_sort
    print("Bubble Sort")
    arr = [64, 25, 12, 34, 22]
    bubble_sort = BubbleSort(arr)
    bubble_sort.bubble_sort()
    bubble_sort.display()
    print()

    # quick_sort
    print("Quick Sort")
    quick_sort = QuickSort([5, 4, 8, 1, 9, 3])
    quick_sort.display()
    print()

    # palindrome
    print("Palindrome")
    words = ["madam", "hello"]
    for word in words:
        palindrome = Palindrome(word)
        palindrome.display()
        print()

    # factorial
    print("Factorial")
    numbers = [5, 0]
    for n in numbers:
        factorial = Factorial(n)
        factorial.display()
    print()

    # sum_of_2_no
    print("Sum of 2 No.")
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([1, 3, 5, 8],   6),
    ]
    for num, target in test_cases:
        sum2 = Sum_of_Two(num, target)
        sum2.display()
        print()

    # sum_of_3_no
    print("Sum of 3 No.")
    test_cases_3 = [
        ([1, 2, 3, 4, 0, -1],               4),
        ([0.5, 1.5, 2.0, 3.0, -1.0, -0.5],  4),
    ]
    for nums, target in test_cases_3:
        Sum_of_three(nums, target).display()
        print()

    # sum_of_4_no
    print("Sum of 4 No.")
    test_cases_4 = [
        ([1, 0, -1, 0, -2, 2],  0),
        ([2, 4, 5, 8, 2, 4],    12),
    ]
    for nums, target in test_cases_4:
        sum_of_four(nums, target).display()
        print()

    # water_example
    print("Water Task")
    heights = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 2, -3, 4],
        [0, 0, 0, 0],
        [-5, -3, -6, -2],
        [3, 7],
        [1, 1],
    ]
    MaxWater(heights).display()
    print()

    # Combination_Sum
    print("Combination Sum")
    for candidates, target in [
        ([1, 3, 2, 2, 5], 4),
        ([2, 3, 6, 7],    7),
    ]:
        Combination_Sum(candidates, target).display()
        print()

    # median_task
    print("Median")
    test_cases = [
        ([1, 3, 5],       [2, 4, 6],     "Normal Case         "),
        ([0, 0, 0],       [0, 0, 0],     "All Zeros           "),
        ([-3, -1, 2],     [-2, 1, 4],    "Negative & Positive "),
        ([1, 3, 5],       [],            "nums2 Empty         "),
        ([1, 2, 3, 4],    [5, 6],        "Different Sizes     "),
        ([1],             [2],           "Single Each         "),
        ([-5, -3, -1],    [-4, -2, -1],  "All Negative        "),
        ([1, 3, 56, 100], [2, 3, 4, 98], "Repeated Numbers    "),
    ]
    for nums1, nums2, label in test_cases:
        print(f"{label}")
        MedianSorted(nums1, nums2).display()
        print()
        
    #Sort

    sort = Sort([5, 4, 8, 1, 9, 3])
    print("Before sort:", sort.original)
    print("Bubble sort:", sort.bubble_sort())
    print("Quick sort: ", sort.quick_sort())
    
