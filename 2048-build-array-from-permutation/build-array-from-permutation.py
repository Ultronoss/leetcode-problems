class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            val = nums[i]
            ans.append(nums[val])
        return ans