class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        trapped_water = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(height[left], left_max)
                trapped_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                trapped_water += right_max - height[right]

        return trapped_water