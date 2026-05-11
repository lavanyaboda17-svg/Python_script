# module.py

from sort import Sort
from palindrome import Palindrome
from factorial import Factorial
from sum import SubsetSum
from max_water import MaxWater
from Combination_Sum import Combination_Sum
from median_sorted import MedianSorted
from stack import ValidParentheses


if __name__ == "__main__":

    Sort([5, 4, 8, 1, 9, 3]).bubble_sort()
    Sort([5, 4, 8, 1, 9, 3]).quick_sort()

    for word in ["madam", "hello"]:
        Palindrome(word).palindrome()

    for n in [5, 0]:
        Factorial(n).factorial()

    for nums, target in [
        ([2, 7, 11, 15], 9),
        ([1, 3, 5, 8], 6)
    ]:
        SubsetSum(nums, target).two_sum()

    for nums, target in [
        ([1, 2, 3, 4, 0, -1], 4)
    ]:
        SubsetSum(nums, target).three_sum()

    for nums, target in [
        ([1, 0, -1, 0, -2, 2], 0)
    ]:
        SubsetSum(nums, target).four_sum()

    for height in [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1]
    ]:
        MaxWater(height).maxArea()

    for candidates, target in [
        ([2, 3, 6, 7], 7)
    ]:
        Combination_Sum(candidates, target).combinationSum()

    for nums1, nums2 in [
        ([1, 3, 5], [2, 4, 6]),
        ([1], [2])
    ]:
        MedianSorted(nums1, nums2).medianSortedArray()

    for s in [
        # Basic Valid
        "()",
        "[]",
        "{}",
        "()[]{}",
        "{[()]}",
        "{[]}",

        # Basic Invalid
        "(]",
        "([)]",
        "(}",
        "{)",

        # Empty String
        "",

        # Only Opening Brackets
        "(((",
        "{{{",
        "[[[",
        "(([]",

        # Only Closing Brackets
        ")))",
        "}}}",
        "]]]",

        # Single Characters
        "(",
        ")",
        "{",
        "}",
        "[",
        "]",

        # Deeply Nested
        "((((((()))))))",
        "{[({[({[]})]})}",
        "({[({[{}]})]})[]",

        # Long Mixed Valid
        "(){}[](){}[](){}[]",

        # Interleaved Invalid
        "([)]",
        "{[}]",
        "[(])",

        # Non-Bracket Characters
        "(hello)",
        "{ }",
    ]:
        ValidParentheses(s).is_valid()