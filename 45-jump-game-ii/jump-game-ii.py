class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        l = 0
        r = 0 # initiate left and right index pointer for each jump

        while r < len(nums) - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])

            l = l + 1
            r = far
            result += 1

        return result
