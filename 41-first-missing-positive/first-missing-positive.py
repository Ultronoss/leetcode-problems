class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)

        # Starting from 1, check for each number if it's in the set
        i = 1
        while True:
            if i not in num_set:
                return i
            i += 1