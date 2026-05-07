class MedianSorted:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def medianSortedArray(self):
        i, j  = 0, 0
        total = len(self.nums1) + len(self.nums2)
        mid   = total // 2
        prev, curr = 0, 0

        for _ in range(mid + 1):
            prev = curr
            if i < len(self.nums1) and (j >= len(self.nums2) or self.nums1[i] <= self.nums2[j]):
                curr = self.nums1[i]
                i += 1
            else:
                curr = self.nums2[j]
                j += 1

        if total % 2 == 1:       # odd  → middle element
            return float(curr)
        else:                     # even → average of two middles
            return (prev + curr) / 2.0

    def display(self):
        result = self.medianSortedArray()
        print(f"Nums1  : {self.nums1}")
        print(f"Nums2  : {self.nums2}")
        print(f"Median : {result}")