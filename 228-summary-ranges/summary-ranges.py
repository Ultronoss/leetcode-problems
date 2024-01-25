class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        start = nums[0]
        end = None
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1: # increase range
                # print(nums[i])
                end = nums[i]
            else:
                if end != None:
                    res.append(str(start)+'->'+str(end))
                    end = None
                else:
                    res.append(str(start))
                start = nums[i]
        if end != None:
            res.append(str(start)+'->'+str(end))
        else:
            res.append(str(start))
        return res

                