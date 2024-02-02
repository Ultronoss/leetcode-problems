class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left_peaks = [0] * len(height)
        right_peaks = [0] * len(height)
        l,r = 1,len(height) - 2
        while l < len(height) and r >= 0:
            left_peaks[l] = max(height[l-1], left_peaks[l-1])
            right_peaks[r] = max(height[r+1], right_peaks[r+1])
            l += 1
            r -= 1
        for idx in range(len(height)):
            result +=  max(min(left_peaks[idx], right_peaks[idx]) - height[idx], 0)
        
        return result            
            