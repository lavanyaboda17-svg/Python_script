from display import display

class Sort:
    def __init__(self, arr):
        self.arr      = arr
        self.original = arr.copy()

    @display("Bubble Sort", header="Sort")
    def bubble_sort(self):
        print(f"Before Sort : {self.original}")   # ← print before
        arr = self.arr.copy()
        n   = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr                                # ← decorator prints "Bubble Sort : result"

    @display("Quick Sort")
    def quick_sort(self):
        print(f"Before Sort : {self.original}")   # ← print before
        return self._quick(self.arr.copy())       # ← decorator prints "Quick Sort : result"

    def _quick(self, arr):
        if len(arr) <= 1:
            return arr
        pivot   = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        bigger  = [x for x in arr[1:] if x > pivot]
        return self._quick(smaller) + [pivot] + self._quick(bigger)