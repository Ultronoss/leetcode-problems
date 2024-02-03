class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        def combine(l1,l2):
            return [l1[0],max(l1[1],l2[1])]

        for i in sorted(intervals, key=lambda i: i[0]):
            if (res and i[0] <= res[-1][1]):
                res[-1] = combine(res[-1],i)
            else :
                res += [i]            
        return res