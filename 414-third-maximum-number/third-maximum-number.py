import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        for num in set(nums):
            heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)
        if len(heap) < 3:
            return max(heap)
        return heap[0]