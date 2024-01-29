class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def find_next_greater(num, nums):
            if not nums:
                return -1
            if num < nums[0]:
                return nums[0]
            return find_next_greater(num, nums[1:])

        return [find_next_greater(num, nums2[nums2.index(num):]) for num in nums1]