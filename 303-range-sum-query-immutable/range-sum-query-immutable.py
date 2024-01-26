import itertools
class NumArray:

    def __init__(self, nums: List[int]):
        self.cumulative_sum = [0] + list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)