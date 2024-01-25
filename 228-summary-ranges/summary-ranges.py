class Solution:
    def convert_to_string(self,a,b):
        if a==b:
            return str(a)
        return f"{a}->{b}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        res = []    
        range=[]
        c=nums[0]
        for n in nums:
            if n == c:
                range.append(n)
                c+=1
            else:
                res.append(self.convert_to_string(range[0],range[-1]))
                range=[n]
                c=n+1
        res.append(self.convert_to_string(range[0],range[-1]))
        return res