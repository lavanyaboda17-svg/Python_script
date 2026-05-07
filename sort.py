# sort.py
class Sort:
    def __init__(self, arr):
        self.arr      = arr
        self.original = arr.copy()

    def bubble_sort(self):
        arr = self.arr.copy()
        n   = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def quick_sort(self, arr=None):
        if arr is None:
            arr = self.arr.copy()
        if len(arr) <= 1:
            return arr
        pivot   = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        bigger  = [x for x in arr[1:] if x > pivot]
        return self.quick_sort(smaller) + [pivot] + self.quick_sort(bigger)