class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                # newInterval is to the right of the current interval, so we just append the current interval
                merged.append(interval)
            elif newInterval[1] < interval[0]:
                # newInterval is to the left of the current interval, so we append newInterval and update it to be the current interval
                merged.append(newInterval)
                newInterval = interval
            else:
                # newInterval overlaps with the current interval, so we merge them
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        # Append the last interval
        merged.append(newInterval)
        return merged