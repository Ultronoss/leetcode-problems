class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])

        merged = [intervals[0]]
        for cur in intervals:
            if cur[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], cur[1])
            else:
                merged.append(cur)
        return merged