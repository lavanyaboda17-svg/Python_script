#WATER EXAMPLE
def maxArea(height):
    length_of_height= len(height)
    if length_of_height == [1,0] or all(h <= 0 for h in height):
        return 0
    if length_of_height == 2:
        area = min(height[0], height[1]) * 1
        print("Only 2 walls area is :",area)     #(maxArea([3, 7])) = 3
        return area  
    left, right = 0,length_of_height - 1   # 9-1 = 8
    max_water = 0 
    while left < right:
        # Calculate current area
        width = right - left #left=1, right=8 → width = 8-1 = 7
        current_area = min(height[left], height[right]) * width
        max_water = max(max_water, current_area)
         # Move the pointer with the shorter height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

# Test
