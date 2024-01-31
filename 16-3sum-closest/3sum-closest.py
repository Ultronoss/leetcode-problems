class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closedsum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(target - sum) < abs(target - closedsum):
                    closedsum = sum
                if (sum > target):
                    right -= 1
                else:
                    left += 1
        return closedsum 