# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1

        index = count - n
        node = ListNode()
        node.next = head
        tmp = node
        for i in range(count):
            if i == index:
                tmp.next = tmp.next.next if tmp.next else None
            else:
                tmp = tmp.next

        return node.next
