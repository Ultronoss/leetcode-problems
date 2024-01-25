class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        l = r = 0
        ans = []
        while r != len(nums) - 1:
            if nums[r] == nums[r + 1] - 1:
                r += 1
            else:
                if r == l:
                    ans.append(str(nums[l]))
                else:
                    ans.append(f"{nums[l]}->{nums[r]}")
                r += 1
                l = r

        if r == l:
            ans.append(str(nums[l]))
        else:
            ans.append(f"{nums[l]}->{nums[r]}")
            
        return ans
        
