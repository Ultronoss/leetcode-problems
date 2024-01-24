class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        for num, count in frequency.items():
            if count == 1:
                return num