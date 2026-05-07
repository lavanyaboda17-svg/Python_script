class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.original = arr.copy()

    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.arr

    def display(self):
        print("Before Sort:", self.original)
        print("After Sort: ", self.arr)