class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        perm = []

        def dfs(i): 
            if i == len(nums): 
                ans.append(perm[:])
                return 
            
            for num in nums: 
                if num not in perm: 
                    perm.append(num)
                    dfs(i+1)
                    perm.pop()
            
        
        dfs(0)
        return ans