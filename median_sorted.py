from display import display

class MedianSorted:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    @display("Median", header="Median")              
    def medianSortedArray(self):
        print(f"Nums1   : {self.nums1}")
        print(f"Nums2   : {self.nums2}")
        merged = sorted(self.nums1 + self.nums2)
        n      = len(merged)
        mid    = n // 2
        if n % 2 == 1:
            return float(merged[mid])
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0