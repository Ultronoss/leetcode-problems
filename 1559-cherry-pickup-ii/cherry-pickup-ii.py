class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[-1]*cols for _1 in range(cols)] for _2 in range(rows)]
        
        def helper(r, c1, c2):
            if r == rows:
                return 0
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]
            result = 0
            for new_c1 in [c1, c1+1, c1-1]:
                for new_c2 in [c2, c2+1, c2-1]:
                    if new_c1>=0 and new_c1<cols and new_c2>=0 and new_c2<cols:
                        result = max(result, helper(r+1, new_c1, new_c2))
            result += grid[r][c1]
            if c1 != c2:
                result += grid[r][c2]
            dp[r][c1][c2] = result
            return result
        
        return helper(0, 0, cols-1)