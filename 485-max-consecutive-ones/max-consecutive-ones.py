class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                res.append(count)
                count = 0
        res.append(count)
        res.sort(reverse=True)
        return res[0]