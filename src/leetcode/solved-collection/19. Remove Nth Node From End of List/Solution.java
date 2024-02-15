/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 0;
        ListNode temp = head;
        while(temp != null) {
            temp = temp.next;
            count++;
        }

        int index = count - n;

        ListNode node = new ListNode();
        node.next = head;

        ListNode tmp = node;
        for(int i = 0; i < count; i++) {
            if(i == index) {
                tmp.next = tmp.next != null ? tmp.next.next : null;
            } else {
                tmp = tmp.next;
            }                 
        }

        return node.next;
    }
}
