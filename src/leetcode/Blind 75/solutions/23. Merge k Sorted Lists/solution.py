# Time Complexity: O(nlogk)
# Space Complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(heap)
        head = curr = ListNode()

        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(heap, (node.val, idx))
        return head.next
        
