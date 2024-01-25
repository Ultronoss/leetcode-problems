class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
    
        ranges = []
        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                ranges.append(f"{start}->{end}" if start != end else str(start))
                start = end = num

        ranges.append(f"{start}->{end}" if start != end else str(start))

        return ranges