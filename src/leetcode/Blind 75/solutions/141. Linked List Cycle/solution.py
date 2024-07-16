# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        temp = head
        hash_set = set()

        while temp:
            if temp in hash_set:
                return True

            hash_set.add(temp)
            temp = temp.next

        return False
        
