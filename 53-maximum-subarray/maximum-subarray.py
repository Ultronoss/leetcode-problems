class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        cursum=0
        for num in nums:
            cursum+=num
            if cursum >maxsum:
                maxsum=cursum
            if cursum < 0:
                cursum=0
        return maxsum