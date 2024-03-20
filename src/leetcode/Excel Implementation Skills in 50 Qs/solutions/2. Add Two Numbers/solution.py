# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        stack = []
        carry = 0
        while stack1 or stack2:
            current_sum = carry + (stack1.pop(0) if stack1 else 0) + (stack2.pop(0) if stack2 else 0)
            if current_sum <= 9:
                stack.append(current_sum)
                carry = 0
            else:
                carry = 1
                stack.append(current_sum % 10)
        
        if carry > 0:
            stack.append(carry)

        result = ListNode()
        cur = result
        while stack:
            cur.val = stack.pop(0)
            cur.next = ListNode() if stack else None
            cur = cur.next
        return result
