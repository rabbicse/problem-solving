/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode();
        dummy->next = head;

        ListNode* fast = head;

        int length = 0;
        while(fast != NULL) {
            length++;
            fast = fast->next;
        }

        length -= n;
        fast = dummy;
        while(length > 0) {            
            fast = fast->next;
            length--;
        }

        fast->next = fast->next->next;
        

        return dummy->next;
    }
};
