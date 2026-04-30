def medianSortedArray(nums1, nums2):
    i, j = 0, 0
    total = len(nums1) + len(nums2)
    mid = total // 2
    prev, curr = 0, 0

    for _ in range(mid + 1): #(1,2,3/ 0,1,2,3 index)
        prev = curr
        if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    if total % 2 == 1:
        return float(curr)
    else:
        return (prev + curr) / 2.0

# Test
nums1 = [1, 3, 5]
nums2 = []
print("Median:", medianSortedArray(nums1, nums2))  