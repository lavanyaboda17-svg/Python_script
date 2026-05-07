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

#Bubble_Sort
print("Bubble_Sort")
obj = BubbleSort()
obj.sort()
obj.display()
print()

#Quick_Sort
print("Quick_Sort")
obj = QuickSort()
obj.display()
print()

#Palindrome
print("Palindrome")
obj = Palindrome()
obj.display()
print()

#factorial
print("Factorial")
obj = Factorial()     
obj.display()
print()

#Sum_of_2_no.
print("Two_Sum")
obj = Sum_of_Two()
obj.display()
print()

#Sum_of_3_no.
print("Three_Sum")
obj = Sum_of_three()
obj.display()
print()

#Sum_of_4_no.
print("Four_Sum")
obj = sum_of_four()
obj.display()
print()

#Water_ex
print("Water Example")
obj = MaxWater()
obj.display()
print()

#CombinatationSum
obj = Combination_Sum()
obj.display()   

#Median_task
obj = MedianSorted()
obj.display()
