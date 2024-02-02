class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        if len(res) == 1:
            res += res
        if len(res) > 0:
            return [res[0], res[-1]]
        else:
            return [-1, -1] 