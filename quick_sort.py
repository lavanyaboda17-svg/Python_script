class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.original = arr.copy()

    def quick_sort(self, arr):
        if len(arr) <= 1:        # base case: single item is already sorted
            return arr
        pivot   = arr[0]                             # first item as pivot
        smaller = [x for x in arr[1:] if x <= pivot] # items <= pivot go left
        bigger  = [x for x in arr[1:] if x > pivot]  # items >  pivot go right
        return self.quick_sort(smaller) + [pivot] + self.quick_sort(bigger)

    def display(self):
        print("Before Sort:", self.original)
        print("After Sort: ", self.quick_sort(self.arr))