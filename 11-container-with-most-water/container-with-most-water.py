class Solution:
    def maxArea(self, height: List[int], right = 0, left = 0) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculating the area
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # Updating the maximum area if necessary
            max_area = max(max_area, area)

            # Moving the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
