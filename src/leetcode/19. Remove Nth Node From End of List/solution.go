/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    count := 0
    temp := head
    for temp != nil {
        temp = temp.Next
        count++
    }

    index := count - n

    node := &ListNode{}
    node.Next = head
    tmp := node
    for i := 0; i < count; i++ {
        if i == index {
            if tmp.Next != nil {
                tmp.Next = tmp.Next.Next
            } else {
                tmp.Next = nil
            }
        } else if tmp.Next != nil {
            tmp = tmp.Next
        }
    }
    return node.Next
}
