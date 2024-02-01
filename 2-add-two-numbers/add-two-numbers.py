# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self,l1,l2,carry):
        if not l1 and not l2:
            if carry > 0:
                return ListNode(carry)
            return None
        
        if l1 and not l2:
            val = (l1.val+carry)
            carry = val//10
            head = ListNode(val%10)
            head.next = self.helper(l1.next,l2,carry)
            return head

        if l2 and not l1:
            val = (l2.val+carry)
            carry = val//10
            head = ListNode(val%10)
            head.next = self.helper(l1,l2.next,carry)
            return head
            
        val = (l1.val+l2.val+carry)
        carry = val//10
        head = ListNode(val%10)
        head.next = self.helper(l1.next,l2.next,carry)
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(l1,l2,0)