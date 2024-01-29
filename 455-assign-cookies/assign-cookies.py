class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        return helper(g, s, 0, 0)

def helper(g, s, i, j):
    if i == len(g) or j == len(s):
        return 0
    if s[j] >= g[i]:
        return 1 + helper(g, s, i+1, j+1)
    else:
        return helper(g, s, i, j+1)