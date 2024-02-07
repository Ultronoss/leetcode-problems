class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                back(nums[:i] + nums[i + 1:], path + [nums[i]])
        res = []
        back(nums, [])
        return res