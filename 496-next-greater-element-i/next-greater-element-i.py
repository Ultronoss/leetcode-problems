class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # Iterate over nums2 in reverse order
        for num in reversed(nums2):
            # Pop elements from the stack which are less than the current element
            while stack and stack[-1] < num:
                stack.pop()
            # If the stack is not empty, the top element is the next greater element
            # If the stack is empty, there is no next greater element
            next_greater[num] = stack[-1] if stack else -1
            # Push the current element to the stack
            stack.append(num)

        # Return the next greater element for each element in nums1
        return [next_greater[num] for num in nums1]

        