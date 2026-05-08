from display import display

class MaxWater:
    def __init__(self, height):
        self.height = height

    @display("Max Area",header="Max Area")
    def maxArea(self):
        print(f"Height  : {self.height}")       # ← print before result
        height = self.height
        n      = len(height)
        if n <= 1 or all(h <= 0 for h in height):
            return 0
        left, right, max_water = 0, n - 1, 0
        while left < right:
            area      = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, area)
            if height[left] < height[right]:
                left  += 1
            else:
                right -= 1
        return max_water