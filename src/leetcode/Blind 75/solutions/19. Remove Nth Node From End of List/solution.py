# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        # index to remove
        index = count - n

        node = ListNode()
        node.next = head
        temp = node
        for _ in range(index):
            temp = temp.next

        if temp and temp.next:
            temp.next = temp.next.next
        return node.next
        
