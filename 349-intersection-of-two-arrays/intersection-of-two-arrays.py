class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            for j in nums2:
                if nums1[i] == j:
                    res.append(nums1[i])
        return set(res)