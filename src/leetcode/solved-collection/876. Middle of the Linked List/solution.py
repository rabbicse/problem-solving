# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp.next:
            temp = temp.next
            count += 1

        mid = int(count / 2) if count % 2 == 0 else int(count / 2) + 1

        for i in range(mid):
            head = head.next

        return head
