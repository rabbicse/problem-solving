/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    count := 0
    temp := head
    for temp.Next != nil {
        temp = temp.Next
        count++
    }

    mid := 0
    if count % 2 == 0 { 
        mid = count / 2
    } else {
        mid = (count / 2) + 1
    }            

    for i := 0; i < mid; i++ {
        head = head.Next
    }

    return head
}
