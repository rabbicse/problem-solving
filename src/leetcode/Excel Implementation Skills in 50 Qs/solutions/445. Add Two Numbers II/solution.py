# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        dummy = ListNode()
        while stack1 or stack2 or carry > 0:
            stack1_val = stack1.pop() if stack1 else 0
            stack2_val = stack2.pop() if stack2 else 0
            current_sum = stack1_val + stack2_val + carry
            print(stack1_val, stack2_val, current_sum)
        
            if current_sum <= 9:
                dummy.val = current_sum
                carry = 0
            else:
                dummy.val = current_sum % 10
                carry = 1
            
            head = ListNode(carry)
            head.next = dummy
            dummy = head

        return dummy.next
