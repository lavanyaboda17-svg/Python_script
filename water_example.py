class MaxWater:
    def __init__(self, heights):
        self.heights = heights   # list of height arrays to test

    def maxArea(self, height):
        n = len(height)

        if n <= 1:                        # need at least 2 walls
            return 0
        if all(h <= 0 for h in height):  # all negative or zero
            return 0
        if n == 2:                        # only 2 walls
            return max(0, min(height[0], height[1]))

        # ── Two Pointer ──────────────────────────
        left      = 0
        right     = n - 1
        max_water = 0

        while left < right:
            width        = right - left
            current_area = min(height[left], height[right]) * width
            max_water    = max(max_water, current_area)

            if height[left] < height[right]:
                left  += 1    # move smaller wall inward
            else:
                right -= 1    # move smaller wall inward
        return max_water

    def display(self):
        for i, h in enumerate(self.heights):
            print(f"height_{i}  : {h}")
            print(f"max area   : {self.maxArea(h)}")
            print()